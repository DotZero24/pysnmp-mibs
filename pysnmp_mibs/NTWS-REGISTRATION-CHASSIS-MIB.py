if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntwsRegistration,=mibBuilder.importSymbols('NTWS-ROOT-MIB','ntwsRegistration')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntwsRegistrationChassisMib=ModuleIdentity((1,3,6,1,4,1,45,6,1,3,5))
if mibBuilder.loadTexts:ntwsRegistrationChassisMib.setRevisions(('2007-08-22 00:00',))
_NtwsChassisComponents_ObjectIdentity=ObjectIdentity
ntwsChassisComponents=_NtwsChassisComponents_ObjectIdentity((1,3,6,1,4,1,45,6,1,3,4))
_NtwsChasCompPowerSupplies_ObjectIdentity=ObjectIdentity
ntwsChasCompPowerSupplies=_NtwsChasCompPowerSupplies_ObjectIdentity((1,3,6,1,4,1,45,6,1,3,4,1))
_NtwsChasCompPowerSupply1_ObjectIdentity=ObjectIdentity
ntwsChasCompPowerSupply1=_NtwsChasCompPowerSupply1_ObjectIdentity((1,3,6,1,4,1,45,6,1,3,4,1,1))
_NtwsChasCompPowerSupply2_ObjectIdentity=ObjectIdentity
ntwsChasCompPowerSupply2=_NtwsChasCompPowerSupply2_ObjectIdentity((1,3,6,1,4,1,45,6,1,3,4,1,2))
_NtwsChasCompFans_ObjectIdentity=ObjectIdentity
ntwsChasCompFans=_NtwsChasCompFans_ObjectIdentity((1,3,6,1,4,1,45,6,1,3,4,2))
_NtwsChasCompFan1_ObjectIdentity=ObjectIdentity
ntwsChasCompFan1=_NtwsChasCompFan1_ObjectIdentity((1,3,6,1,4,1,45,6,1,3,4,2,1))
_NtwsChasCompFan2_ObjectIdentity=ObjectIdentity
ntwsChasCompFan2=_NtwsChasCompFan2_ObjectIdentity((1,3,6,1,4,1,45,6,1,3,4,2,2))
_NtwsChasCompFan3_ObjectIdentity=ObjectIdentity
ntwsChasCompFan3=_NtwsChasCompFan3_ObjectIdentity((1,3,6,1,4,1,45,6,1,3,4,2,3))
mibBuilder.exportSymbols('NTWS-REGISTRATION-CHASSIS-MIB',**{'ntwsChassisComponents':ntwsChassisComponents,'ntwsChasCompPowerSupplies':ntwsChasCompPowerSupplies,'ntwsChasCompPowerSupply1':ntwsChasCompPowerSupply1,'ntwsChasCompPowerSupply2':ntwsChasCompPowerSupply2,'ntwsChasCompFans':ntwsChasCompFans,'ntwsChasCompFan1':ntwsChasCompFan1,'ntwsChasCompFan2':ntwsChasCompFan2,'ntwsChasCompFan3':ntwsChasCompFan3,'ntwsRegistrationChassisMib':ntwsRegistrationChassisMib})