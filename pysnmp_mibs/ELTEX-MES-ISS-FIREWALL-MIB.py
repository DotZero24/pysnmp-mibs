_E='TruthValue'
_D='ifIndex'
_C='IF-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_E)
eltMesIssFwlMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,27))
if mibBuilder.loadTexts:eltMesIssFwlMIB.setRevisions(('2021-04-21 00:00',))
_EltMesIssFwlObjects_ObjectIdentity=ObjectIdentity
eltMesIssFwlObjects=_EltMesIssFwlObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,27,1))
_EltMesIssFwlGlobals_ObjectIdentity=ObjectIdentity
eltMesIssFwlGlobals=_EltMesIssFwlGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,139,27,1,1))
_EltMesIssFwlNotificationInterval_Type=Integer32
_EltMesIssFwlNotificationInterval_Object=MibScalar
eltMesIssFwlNotificationInterval=_EltMesIssFwlNotificationInterval_Object((1,3,6,1,4,1,35265,1,139,27,1,1,1),_EltMesIssFwlNotificationInterval_Type())
eltMesIssFwlNotificationInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssFwlNotificationInterval.setStatus(_A)
_EltMesIssFwlTcpSynLimit_ObjectIdentity=ObjectIdentity
eltMesIssFwlTcpSynLimit=_EltMesIssFwlTcpSynLimit_ObjectIdentity((1,3,6,1,4,1,35265,1,139,27,1,2))
class _EltMesIssFwlTcpSynLimitEnable_Type(TruthValue):defaultValue=2
_EltMesIssFwlTcpSynLimitEnable_Type.__name__=_E
_EltMesIssFwlTcpSynLimitEnable_Object=MibScalar
eltMesIssFwlTcpSynLimitEnable=_EltMesIssFwlTcpSynLimitEnable_Object((1,3,6,1,4,1,35265,1,139,27,1,2,1),_EltMesIssFwlTcpSynLimitEnable_Type())
eltMesIssFwlTcpSynLimitEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssFwlTcpSynLimitEnable.setStatus(_A)
_EltMesIssFwlTcpSynLimitInterfaceTable_Object=MibTable
eltMesIssFwlTcpSynLimitInterfaceTable=_EltMesIssFwlTcpSynLimitInterfaceTable_Object((1,3,6,1,4,1,35265,1,139,27,1,2,2))
if mibBuilder.loadTexts:eltMesIssFwlTcpSynLimitInterfaceTable.setStatus(_A)
_EltMesIssFwlTcpSynLimitInterfaceEntry_Object=MibTableRow
eltMesIssFwlTcpSynLimitInterfaceEntry=_EltMesIssFwlTcpSynLimitInterfaceEntry_Object((1,3,6,1,4,1,35265,1,139,27,1,2,2,1))
eltMesIssFwlTcpSynLimitInterfaceEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:eltMesIssFwlTcpSynLimitInterfaceEntry.setStatus(_A)
_EltMesIssFwlTcpSynLimitValue_Type=Integer32
_EltMesIssFwlTcpSynLimitValue_Object=MibTableColumn
eltMesIssFwlTcpSynLimitValue=_EltMesIssFwlTcpSynLimitValue_Object((1,3,6,1,4,1,35265,1,139,27,1,2,2,1,1),_EltMesIssFwlTcpSynLimitValue_Type())
eltMesIssFwlTcpSynLimitValue.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssFwlTcpSynLimitValue.setStatus(_A)
_EltMesIssFwlNotifications_ObjectIdentity=ObjectIdentity
eltMesIssFwlNotifications=_EltMesIssFwlNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,139,27,2))
mibBuilder.exportSymbols('ELTEX-MES-ISS-FIREWALL-MIB',**{'eltMesIssFwlMIB':eltMesIssFwlMIB,'eltMesIssFwlObjects':eltMesIssFwlObjects,'eltMesIssFwlGlobals':eltMesIssFwlGlobals,'eltMesIssFwlNotificationInterval':eltMesIssFwlNotificationInterval,'eltMesIssFwlTcpSynLimit':eltMesIssFwlTcpSynLimit,'eltMesIssFwlTcpSynLimitEnable':eltMesIssFwlTcpSynLimitEnable,'eltMesIssFwlTcpSynLimitInterfaceTable':eltMesIssFwlTcpSynLimitInterfaceTable,'eltMesIssFwlTcpSynLimitInterfaceEntry':eltMesIssFwlTcpSynLimitInterfaceEntry,'eltMesIssFwlTcpSynLimitValue':eltMesIssFwlTcpSynLimitValue,'eltMesIssFwlNotifications':eltMesIssFwlNotifications})