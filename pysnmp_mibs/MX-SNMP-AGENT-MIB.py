_H='snmpAgentAccessGroupVer1'
_G='snmpAgentAccess'
_F='snmpAgentEnable'
_E='read-write'
_D='Integer32'
_C='MxEnableState'
_B='MX-SNMP-AGENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixConfig,=mibBuilder.importSymbols('MX-SMI','mediatrixConfig')
MxEnableState,=mibBuilder.importSymbols('MX-TC',_C)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
snmpAgentMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,150))
if mibBuilder.loadTexts:snmpAgentMIB.setRevisions(('2005-04-28 00:00','2004-02-13 00:00'))
_SnmpAgentMIBObjects_ObjectIdentity=ObjectIdentity
snmpAgentMIBObjects=_SnmpAgentMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,150,1))
class _SnmpAgentEnable_Type(MxEnableState):defaultValue=1
_SnmpAgentEnable_Type.__name__=_C
_SnmpAgentEnable_Object=MibScalar
snmpAgentEnable=_SnmpAgentEnable_Object((1,3,6,1,4,1,4935,15,150,1,1),_SnmpAgentEnable_Type())
snmpAgentEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpAgentEnable.setStatus(_A)
class _SnmpAgentAccess_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('lanOnly',0),('wanOnly',1),('all',2)))
_SnmpAgentAccess_Type.__name__=_D
_SnmpAgentAccess_Object=MibScalar
snmpAgentAccess=_SnmpAgentAccess_Object((1,3,6,1,4,1,4935,15,150,1,5),_SnmpAgentAccess_Type())
snmpAgentAccess.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpAgentAccess.setStatus(_A)
_SnmpAgentConformance_ObjectIdentity=ObjectIdentity
snmpAgentConformance=_SnmpAgentConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,150,2))
_SnmpAgentCompliances_ObjectIdentity=ObjectIdentity
snmpAgentCompliances=_SnmpAgentCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,150,2,1))
_SnmpAgentGroups_ObjectIdentity=ObjectIdentity
snmpAgentGroups=_SnmpAgentGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,150,2,5))
snmpAgentAccessGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,150,2,5,5))
snmpAgentAccessGroupVer1.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:snmpAgentAccessGroupVer1.setStatus(_A)
snmpAgentAccessComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,150,2,1,1))
snmpAgentAccessComplVer1.setObjects((_B,_H))
if mibBuilder.loadTexts:snmpAgentAccessComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'snmpAgentMIB':snmpAgentMIB,'snmpAgentMIBObjects':snmpAgentMIBObjects,_F:snmpAgentEnable,_G:snmpAgentAccess,'snmpAgentConformance':snmpAgentConformance,'snmpAgentCompliances':snmpAgentCompliances,'snmpAgentAccessComplVer1':snmpAgentAccessComplVer1,'snmpAgentGroups':snmpAgentGroups,_H:snmpAgentAccessGroupVer1})