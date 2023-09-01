CREATE DEFINER = CURRENT_USER TRIGGER `farmacia`.`usuario_BEFORE_INSERT` BEFORE INSERT ON `usuario` FOR EACH ROW
BEGIN
	
END
CREATE TRIGGER a_mayusculas
	BEFORE INSERT ON `usuario`
		FOR EACH ROW SET
			NEW.nombre = UPPER(NEW.nombre),
      NEW.apellido = UPPER(NEW.apellido),
      NEW.email = UPPER(NEW.email);
