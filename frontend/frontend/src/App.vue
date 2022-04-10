<template>
    
    <div id="app">
        
        <section class="container">
            <div class="popup">
                <form @submit.prevent="submitForm" action="">
                    <div class="title">
                        Estado
                    </div>
                    <div class="inputs-area">
                        <input class="input-text" type="text" name="uf" id="" placeholder="UF" v-model="state.uf">
                        <input class="input-text" type="text" name="nome" id="" placeholder="NOME" v-model="state.nome">
                    </div>
            
                    <div class="bot-side-popup">
                        <button id="cadastrar-commit" type="submit" class="btn btn-outline-success ">Cadastrar</button>
                        <button id="cancelar" type="button" class="btn btn-outline-danger ml-5 ">Limpar</button>
                    </div>
                </form>
            </div>
            <div class="box-table">
                <h1 class="title-table">Estado</h1>
                <div class="line"></div>
                <table>
                    <thead>
                        <tr>
                            <th class="subtitle">UF</th>
                            <th class="subtitle">Nome</th>
                            <th class="subtitle"></th>
                        </tr>
                    </thead>
                
                    <tbody>
                        <tr v-for="estado in estados" :key="estado.id" class="result" @dblclick="$data.state = estado">
                            <th>{{ estado.uf }}</th>
                            <th>{{ estado.nome }}</th>
                            <th class="local-button"> 
                                <button class="button-table green" >Editar <i class="bi bi-pencil-square"></i></button>
                                <button class="button-table red" @click="deleteState(estado)">Deletar <i class="bi bi-trash"></i></button>
                            </th>
                        </tr>
                        
                    </tbody>
                </table>
            </div>
        </section>
        <section class="container">
            <div id="popup-cidade" class="popup">
                <form action="" @submit.prevent="submitForm2">
                    <div class="title">
                        Cidade
                    </div>
                    <div class="inputs-area">
                        <label class="label-drop-down" for="">UF:</label>
                        <select class="drop-down-box" name="" id="" v-model="citie.nome_uf">
                            <option v-for="estado in estados" :key="estado.id" value="">{{ estado.uf }}</option>
                        </select>
                        <input class="input-text" type="text" name="nome" id="" placeholder="NOME" v-model="citie.nome">
                    </div>
            
                    <div class="bot-side-popup">
                        <button id="cadastrar-commit" type="button" class="btn btn-outline-success ">Cadastrar</button>
                        <button id="cancelar" type="button" class="btn btn-outline-danger ml-5 ">Limpar</button>
                    </div>
                </form>
            </div>
            <div class="box-table">
                <h1 class="title-table">Cidade</h1>
                <div class="line"></div>
                <table>
                    <thead>
                        <th class="subtitle">UF</th>
                        <th class="subtitle">Nome</th>
                        <th class="subtitle"></th>
                    
                    </thead>
                    <tbody>
                        <tr v-for="cidade in cidades" :key="cidade.id" class="result">
                            <th>{{ cidade.nome_uf }}</th>
                            <th>{{ cidade.nome }}</th>
                            <th class="local-button"> 
                                <button class="button-table green">Editar <i class="bi bi-pencil-square"></i></button>
                                <button class="button-table red" @click="deleteCitie(cidade)">Deletar <i class="bi bi-trash"></i></button>
                            </th>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

    </div>
</template>

<script>
export default {
    name: 'app',
    data() {
        return {
            state: {},
            citie: {},
        estados: [],
        cidades: []
        }
    },
 
    async created () {
        await this.getStates();
        await this.getCities();
    },
    
        
    methods: {
        submitForm () {
            if (this.state.id === undefined) {
                this.createState();
            } else {
                this.editState();
            }
        },
        submitForm2 () {
            if (this.citie.id === undefined) {
                this.createCitie();
            } else {
                this.editCitie();
            }
        },

        async getStates() {
            const response_estado = await fetch('http://127.0.0.1:8000/app/estado/');
            this.estados = await response_estado.json();

        },

        async getCities() {
            const response_cidade = await fetch('http://127.0.0.1:8000/app/cidade/');
            this.cidades = await response_cidade.json();
 
        },


        async createState(){
            await this.getStates()

            await fetch('http://127.0.0.1:8000/app/estado/', {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.state)
            });
            await this.getStates()
        },

        async editState() {
            await this.getStates()

            await fetch(`http://127.0.0.1:8000/app/estado/${this.state.id}/`, {
                method: 'put',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.state)
            });
            await this.getStates()
            this.state = {};
        },

        async deleteState (state) {
            await this.getStates()

            await fetch(`http://127.0.0.1:8000/app/estado/${state.id}/`, {
                method: 'delete',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.state)
            });
            await this.getStates()
        },


        async createCitie(){
            await this.getStates()

            await fetch('http://127.0.0.1:8000/app/cidade/', {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.citie)
            });
            await this.getCities()
        },

        async editCitie() {
            await this.getCities()

            await fetch(`http://127.0.0.1:8000/app/cidade/${this.citie.id}/`, {
                method: 'put',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.citie)
            });
            await this.getCities()
            this.citie = {};
        },

        async deleteCitie (citie) {
            await this.getStates()

            await fetch(`http://127.0.0.1:8000/app/cidade/${citie.id}/`, {
                method: 'delete',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.citie)
            });
            await this.getCities()
        }
    }
}


//const response_cidade = await fetch('http://127.0.0.1:8000/app/cidade/');
//        this.cidades = await response_cidade.json();
</script>
