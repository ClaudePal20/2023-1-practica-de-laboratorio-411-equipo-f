using System;

public abstract class SprintDesarrollo : ProductBacklog  {
	private int etapas;
	public int Etapas {
		set {
			etapas = value;
		}
	}
	private int reuniones;
	private Incremento busqueda_de_mejoras;
	private DailyScrum reportesDiarios;
	private String equipo;
	private String tiempos;

	public void GetEtapas() {
		throw new System.NotImplementedException("Not implemented");
	}



}
