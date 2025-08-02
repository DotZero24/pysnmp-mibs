if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rbtwsRegistration,=mibBuilder.importSymbols('RBTWS-ROOT-MIB','rbtwsRegistration')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbtwsRegistrationChassisMib=ModuleIdentity((1,3,6,1,4,1,52,4,15,1,3,5))
if mibBuilder.loadTexts:rbtwsRegistrationChassisMib.setRevisions(('2007-08-22 00:00',))
_RbtwsChassisComponents_ObjectIdentity=ObjectIdentity
rbtwsChassisComponents=_RbtwsChassisComponents_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,3,4))
_RbtwsChasCompPowerSupplies_ObjectIdentity=ObjectIdentity
rbtwsChasCompPowerSupplies=_RbtwsChasCompPowerSupplies_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,3,4,1))
_RbtwsChasCompPowerSupply1_ObjectIdentity=ObjectIdentity
rbtwsChasCompPowerSupply1=_RbtwsChasCompPowerSupply1_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,3,4,1,1))
_RbtwsChasCompPowerSupply2_ObjectIdentity=ObjectIdentity
rbtwsChasCompPowerSupply2=_RbtwsChasCompPowerSupply2_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,3,4,1,2))
_RbtwsChasCompFans_ObjectIdentity=ObjectIdentity
rbtwsChasCompFans=_RbtwsChasCompFans_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,3,4,2))
_RbtwsChasCompFan1_ObjectIdentity=ObjectIdentity
rbtwsChasCompFan1=_RbtwsChasCompFan1_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,3,4,2,1))
_RbtwsChasCompFan2_ObjectIdentity=ObjectIdentity
rbtwsChasCompFan2=_RbtwsChasCompFan2_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,3,4,2,2))
_RbtwsChasCompFan3_ObjectIdentity=ObjectIdentity
rbtwsChasCompFan3=_RbtwsChasCompFan3_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,3,4,2,3))
mibBuilder.exportSymbols('RBTWS-REGISTRATION-CHASSIS-MIB',**{'rbtwsChassisComponents':rbtwsChassisComponents,'rbtwsChasCompPowerSupplies':rbtwsChasCompPowerSupplies,'rbtwsChasCompPowerSupply1':rbtwsChasCompPowerSupply1,'rbtwsChasCompPowerSupply2':rbtwsChasCompPowerSupply2,'rbtwsChasCompFans':rbtwsChasCompFans,'rbtwsChasCompFan1':rbtwsChasCompFan1,'rbtwsChasCompFan2':rbtwsChasCompFan2,'rbtwsChasCompFan3':rbtwsChasCompFan3,'rbtwsRegistrationChassisMib':rbtwsRegistrationChassisMib})