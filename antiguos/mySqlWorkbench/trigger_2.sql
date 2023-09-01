CREATE TRIGGER a_mayusculas
	BEFORE UPDATE ON `usuario`
		FOR EACH ROW SET
			NEW.nombre = UPPER(NEW.nombre),
			NEW.apellido = UPPER(NEW.apellido),
			NEW.email = UPPER(NEW.email);