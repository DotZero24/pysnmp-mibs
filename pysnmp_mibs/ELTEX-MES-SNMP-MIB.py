_C='eltSnmpUserEntry'
_B='ELTEX-MES-SNMP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesMng,=mibBuilder.importSymbols('ELTEX-MES','eltMesMng')
usmUserEntry,=mibBuilder.importSymbols('SNMP-USER-BASED-SM-MIB','usmUserEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
AutonomousType,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','TextualConvention')
eltMesSnmp=ModuleIdentity((1,3,6,1,4,1,35265,1,23,1,12))
_EltMesSnmpMIBObjects_ObjectIdentity=ObjectIdentity
eltMesSnmpMIBObjects=_EltMesSnmpMIBObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,12,1))
_EltMesSnmpUser_ObjectIdentity=ObjectIdentity
eltMesSnmpUser=_EltMesSnmpUser_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,12,1,1))
_EltMesSnmpUserGlobals_ObjectIdentity=ObjectIdentity
eltMesSnmpUserGlobals=_EltMesSnmpUserGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,12,1,1,1))
_EltMesSnmpUserConfig_ObjectIdentity=ObjectIdentity
eltMesSnmpUserConfig=_EltMesSnmpUserConfig_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,12,1,1,2))
_EltSnmpUserTable_Object=MibTable
eltSnmpUserTable=_EltSnmpUserTable_Object((1,3,6,1,4,1,35265,1,23,1,12,1,1,2,1))
if mibBuilder.loadTexts:eltSnmpUserTable.setStatus(_A)
_EltSnmpUserEntry_Object=MibTableRow
eltSnmpUserEntry=_EltSnmpUserEntry_Object((1,3,6,1,4,1,35265,1,23,1,12,1,1,2,1,1))
if mibBuilder.loadTexts:eltSnmpUserEntry.setStatus(_A)
_EltSnmpUserPrivProtocol_Type=AutonomousType
_EltSnmpUserPrivProtocol_Object=MibTableColumn
eltSnmpUserPrivProtocol=_EltSnmpUserPrivProtocol_Object((1,3,6,1,4,1,35265,1,23,1,12,1,1,2,1,1,1),_EltSnmpUserPrivProtocol_Type())
eltSnmpUserPrivProtocol.setMaxAccess('read-create')
if mibBuilder.loadTexts:eltSnmpUserPrivProtocol.setStatus(_A)
_EltMesSnmpMIBNotifications_ObjectIdentity=ObjectIdentity
eltMesSnmpMIBNotifications=_EltMesSnmpMIBNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,12,2))
usmUserEntry.registerAugmentions((_B,_C))
eltSnmpUserEntry.setIndexNames(*usmUserEntry.getIndexNames())
mibBuilder.exportSymbols(_B,**{'eltMesSnmp':eltMesSnmp,'eltMesSnmpMIBObjects':eltMesSnmpMIBObjects,'eltMesSnmpUser':eltMesSnmpUser,'eltMesSnmpUserGlobals':eltMesSnmpUserGlobals,'eltMesSnmpUserConfig':eltMesSnmpUserConfig,'eltSnmpUserTable':eltSnmpUserTable,_C:eltSnmpUserEntry,'eltSnmpUserPrivProtocol':eltSnmpUserPrivProtocol,'eltMesSnmpMIBNotifications':eltMesSnmpMIBNotifications})