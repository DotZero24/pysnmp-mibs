if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
trpzRegistration,=mibBuilder.importSymbols('TRAPEZE-NETWORKS-ROOT-MIB','trpzRegistration')
trpzRegistrationChassisMib=ModuleIdentity((1,3,6,1,4,1,14525,3,5))
if mibBuilder.loadTexts:trpzRegistrationChassisMib.setRevisions(('2007-08-22 00:00',))
_TrpzChassisComponents_ObjectIdentity=ObjectIdentity
trpzChassisComponents=_TrpzChassisComponents_ObjectIdentity((1,3,6,1,4,1,14525,3,4))
_TrpzChasCompPowerSupplies_ObjectIdentity=ObjectIdentity
trpzChasCompPowerSupplies=_TrpzChasCompPowerSupplies_ObjectIdentity((1,3,6,1,4,1,14525,3,4,1))
_TrpzChasCompPowerSupply1_ObjectIdentity=ObjectIdentity
trpzChasCompPowerSupply1=_TrpzChasCompPowerSupply1_ObjectIdentity((1,3,6,1,4,1,14525,3,4,1,1))
_TrpzChasCompPowerSupply2_ObjectIdentity=ObjectIdentity
trpzChasCompPowerSupply2=_TrpzChasCompPowerSupply2_ObjectIdentity((1,3,6,1,4,1,14525,3,4,1,2))
_TrpzChasCompFans_ObjectIdentity=ObjectIdentity
trpzChasCompFans=_TrpzChasCompFans_ObjectIdentity((1,3,6,1,4,1,14525,3,4,2))
_TrpzChasCompFan1_ObjectIdentity=ObjectIdentity
trpzChasCompFan1=_TrpzChasCompFan1_ObjectIdentity((1,3,6,1,4,1,14525,3,4,2,1))
_TrpzChasCompFan2_ObjectIdentity=ObjectIdentity
trpzChasCompFan2=_TrpzChasCompFan2_ObjectIdentity((1,3,6,1,4,1,14525,3,4,2,2))
_TrpzChasCompFan3_ObjectIdentity=ObjectIdentity
trpzChasCompFan3=_TrpzChasCompFan3_ObjectIdentity((1,3,6,1,4,1,14525,3,4,2,3))
mibBuilder.exportSymbols('TRAPEZE-NETWORKS-REGISTRATION-CHASSIS-MIB',**{'trpzChassisComponents':trpzChassisComponents,'trpzChasCompPowerSupplies':trpzChasCompPowerSupplies,'trpzChasCompPowerSupply1':trpzChasCompPowerSupply1,'trpzChasCompPowerSupply2':trpzChasCompPowerSupply2,'trpzChasCompFans':trpzChasCompFans,'trpzChasCompFan1':trpzChasCompFan1,'trpzChasCompFan2':trpzChasCompFan2,'trpzChasCompFan3':trpzChasCompFan3,'trpzRegistrationChassisMib':trpzRegistrationChassisMib})