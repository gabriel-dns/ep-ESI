import React, { Component } from 'react'
import './RelatorioPage.css'
import Main from '../template/Main'
import AcademicServices from '../../services/AcademicServices'
import Util from '../../util/util';

const util = new Util();
const academicServices = new AcademicServices()


const headerProps = {
    icon: '',
    title: 'RESULTADOS',
    subtitle: 'Tela de resultados e relatorio'
}

const initialState = {
    user: { name: '', email: '' },
    list: [],
    avaliacao: null,
    dados: {

   
    parecer: {
        orientador: null, 
        aluno: null, 
        textoParecer: '', 
        desempenho: '', 
        ehCcp: false,
        resultado: '' 
    },

    lattes: {
        numeroUsp: null, 
        link: '', 
        dataUltimaAtualizacao: null 
    },

    relatorioAluno: {
        numeroUsp: null, 
        resultadoAvaliacao: '', 
        prazoExameQualificacao: null, 
        prazoEntregaDissertacao: null, 
        atividadesAcademicas: '', 
        resumoAtividades: '', 
        observacoes: '', 
        dificuldadeOrientador: '' 
    },

    disciplinas: [],

    aluno: {
        numeroUsp: null, 
        nomeCompleto: '', 
        email: '',
        dataNascimento: null, 
        localNascimento: '', 
        nacionalidade: '', 
        curso: '', 
        orientador: null, 
        dataMatricula: null,
        dataQualificacao: null, 
        dataProficiencia: null, 
        dataLimiteTrabalhoFinal: null 
    }
}
};


export default class Relatorio extends Component {
    

    state = { ...initialState }

    async componentWillMount() {
        util.autenticacao()
        const urlParams = new URLSearchParams(window.location.search);
        const numeroUsp = urlParams.get('numerousp');
        var response = await academicServices.getdadosAlunos(numeroUsp);

        this.setState({ dados: response })


        if(numeroUsp != null){
            this.setState({ avaliacao: this.blocoAvaliacao() })
        }

        //console.log("PAGINA RELATORIO numeroUsp: " + numeroUsp)
        //window.location.href = "/";
    }

    blocoAvaliacao(){

        return (
            <div className='blocoInformacao'>
            <h2>Avaliacao</h2>
            <label>Forms de avaliação: </label><br />
            <button className="btn btn-warning">
            <a href="https://docs.google.com/forms/d/19pdOvoet4vFr8dyI4A51QZ-CWtJHeCKKDUGpIR8JF5I/viewform?edit_requested=true" target="_blank">
                        <i className="fa fa-envelope"></i>
            </a>
                    </button>
            </div>
        )

    }

    renderTable() {
        const { parecer, lattes, relatorioAluno, disciplinas, aluno } = this.state.dados;
    
        return (
            <div>
                <div className='blocoInformacao'>
                <h2>Dados Aluno</h2>
                <label>Número USP: <spam>{aluno.numeroUsp}</spam></label><br />
                <label>Nome Completo: <spam>{aluno.nomeCompleto}</spam></label><br />
                <label>Email: <spam>{aluno.email}</spam></label><br />
                <label>Curso: <spam>{aluno.curso}</spam></label><br />
                <label>Orientador: <spam>{aluno.orientador}</spam></label><br/>
                <label>Data de Matrícula: <spam>{aluno.dataMatricula}</spam></label><br />
                <label>Realizaçao Qualificação: <spam>{aluno.dataQualificacao}</spam></label><br />
                <label>Realizaçao Proficiência: <spam>{aluno.dataProficiencia}</spam></label><br />
                <label>Data Limite para Trabalho Final: <spam>{aluno.dataLimiteTrabalhoFinal}</spam></label><br />
                </div>


                <div className='blocoInformacao'>
                <h2>Lattes</h2>
                <label>Link: <spam>{lattes.link}</spam></label><br />
                <label>Última Atualização: <spam>{lattes.dataUltimaAtualizacao}</spam></label><br />
                </div>

                <div className='blocoInformacao'>
                <h2>Relatório Aluno</h2>
                <label>Resultado Avaliação: <spam>{relatorioAluno.resultadoAvaliacao ? null: "pendente" }</spam></label><br />
                <label>Prazo Exame Qualificação: <spam>{relatorioAluno.prazoExameQualificacao}</spam></label><br />
                <label>Prazo Entrega Dissertação: <spam>{relatorioAluno.prazoEntregaDissertacao}</spam></label><br />
                <label>Atividades Acadêmicas: <spam>{relatorioAluno.atividadesAcademicas}</spam></label><br />
                <label>Resumo Atividades: <spam>{relatorioAluno.resumoAtividades}</spam></label><br />
                <label>Observações: <spam>{relatorioAluno.observacoes}</spam></label><br />
                <label>Dificuldade com Orientador: <spam>{relatorioAluno.dificuldadeOrientador}</spam></label><br />
                </div>

                <div className='blocoInformacao'>
                <h2>Disciplinas</h2>
                {disciplinas.map(materia =>{
                 return(  
                 <div>
                <label>Nome: <spam>{materia.nome}</spam></label><br />
                <label>Nota: <spam>{materia.nota}</spam></label><br />
                 
                 
                 </div>)
                })}
                
                </div>


                <div className='blocoInformacao'>
                <h2>Parecer</h2>
                <label>Orientador:  <spam>{parecer.orientador}</spam></label><br />
                <label>Aluno:  <spam>{parecer.aluno}</spam></label><br />
                <label>Texto Parecer:  <spam>{parecer.textoParecer}</spam></label><br />
                <label>Desempenho:  <spam>{parecer.desempenho}</spam></label><br />
                <label>Resultado:  <spam>{parecer.resultado}</spam></label><br />
                </div>
                {
                    this.state.avaliacao
                }

            </div>
        );
    };


    
    render() {
        return (
            <Main {...headerProps}>

                {this.renderTable()}
            </Main>
        )
    }
}