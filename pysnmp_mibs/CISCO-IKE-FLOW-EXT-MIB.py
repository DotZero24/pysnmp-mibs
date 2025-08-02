_P='cifeTunnelExtGroup'
_O='cifeGlobalsGroup'
_N='cifeTunnelExtRemoteIdentity'
_M='cifeTunnelExtRemoteIdenType'
_L='cifeTunnelExtLocalIdentity'
_K='cifeTunnelExtLocalIdenType'
_J='cifeClearAllTunnels'
_I='cifeTunnelExtDoi'
_H='Integer32'
_G='cisgIpsSgTunIndex'
_F='cisgIpsSgProtocol'
_E='SnmpAdminString'
_D='CISCO-IPSEC-SIGNALING-MIB'
_C='read-only'
_B='CISCO-IKE-FLOW-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cisgIpsSgProtocol,cisgIpsSgTunIndex=mibBuilder.importSymbols(_D,_F,_G)
CIKEIsakmpDoi,CIPsecPhase1PeerIdentityType=mibBuilder.importSymbols('CISCO-IPSEC-TC','CIKEIsakmpDoi','CIPsecPhase1PeerIdentityType')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoIkeFlowExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,428))
if mibBuilder.loadTexts:ciscoIkeFlowExtMIB.setRevisions(('2004-09-14 00:00',))
_CiscoIkeFlowExtMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoIkeFlowExtMIBNotifs=_CiscoIkeFlowExtMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,428,0))
_CiscoIkeFlowExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIkeFlowExtMIBObjects=_CiscoIkeFlowExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,428,1))
_CifeIkeGlobals_ObjectIdentity=ObjectIdentity
cifeIkeGlobals=_CifeIkeGlobals_ObjectIdentity((1,3,6,1,4,1,9,9,428,1,1))
class _CifeClearAllTunnels_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('clearIPSec',2),('clearFCSP',3)))
_CifeClearAllTunnels_Type.__name__=_H
_CifeClearAllTunnels_Object=MibScalar
cifeClearAllTunnels=_CifeClearAllTunnels_Object((1,3,6,1,4,1,9,9,428,1,1,1),_CifeClearAllTunnels_Type())
cifeClearAllTunnels.setMaxAccess('read-write')
if mibBuilder.loadTexts:cifeClearAllTunnels.setStatus(_A)
_CifeTunnelExtTable_Object=MibTable
cifeTunnelExtTable=_CifeTunnelExtTable_Object((1,3,6,1,4,1,9,9,428,1,2))
if mibBuilder.loadTexts:cifeTunnelExtTable.setStatus(_A)
_CifeTunnelExtEntry_Object=MibTableRow
cifeTunnelExtEntry=_CifeTunnelExtEntry_Object((1,3,6,1,4,1,9,9,428,1,2,1))
cifeTunnelExtEntry.setIndexNames((0,_B,_I),(0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:cifeTunnelExtEntry.setStatus(_A)
_CifeTunnelExtDoi_Type=CIKEIsakmpDoi
_CifeTunnelExtDoi_Object=MibTableColumn
cifeTunnelExtDoi=_CifeTunnelExtDoi_Object((1,3,6,1,4,1,9,9,428,1,2,1,1),_CifeTunnelExtDoi_Type())
cifeTunnelExtDoi.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cifeTunnelExtDoi.setStatus(_A)
_CifeTunnelExtLocalIdenType_Type=CIPsecPhase1PeerIdentityType
_CifeTunnelExtLocalIdenType_Object=MibTableColumn
cifeTunnelExtLocalIdenType=_CifeTunnelExtLocalIdenType_Object((1,3,6,1,4,1,9,9,428,1,2,1,2),_CifeTunnelExtLocalIdenType_Type())
cifeTunnelExtLocalIdenType.setMaxAccess(_C)
if mibBuilder.loadTexts:cifeTunnelExtLocalIdenType.setStatus(_A)
class _CifeTunnelExtLocalIdentity_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CifeTunnelExtLocalIdentity_Type.__name__=_E
_CifeTunnelExtLocalIdentity_Object=MibTableColumn
cifeTunnelExtLocalIdentity=_CifeTunnelExtLocalIdentity_Object((1,3,6,1,4,1,9,9,428,1,2,1,3),_CifeTunnelExtLocalIdentity_Type())
cifeTunnelExtLocalIdentity.setMaxAccess(_C)
if mibBuilder.loadTexts:cifeTunnelExtLocalIdentity.setStatus(_A)
_CifeTunnelExtRemoteIdenType_Type=CIPsecPhase1PeerIdentityType
_CifeTunnelExtRemoteIdenType_Object=MibTableColumn
cifeTunnelExtRemoteIdenType=_CifeTunnelExtRemoteIdenType_Object((1,3,6,1,4,1,9,9,428,1,2,1,4),_CifeTunnelExtRemoteIdenType_Type())
cifeTunnelExtRemoteIdenType.setMaxAccess(_C)
if mibBuilder.loadTexts:cifeTunnelExtRemoteIdenType.setStatus(_A)
class _CifeTunnelExtRemoteIdentity_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CifeTunnelExtRemoteIdentity_Type.__name__=_E
_CifeTunnelExtRemoteIdentity_Object=MibTableColumn
cifeTunnelExtRemoteIdentity=_CifeTunnelExtRemoteIdentity_Object((1,3,6,1,4,1,9,9,428,1,2,1,5),_CifeTunnelExtRemoteIdentity_Type())
cifeTunnelExtRemoteIdentity.setMaxAccess(_C)
if mibBuilder.loadTexts:cifeTunnelExtRemoteIdentity.setStatus(_A)
_CiscoIkeFlowExtMIBConform_ObjectIdentity=ObjectIdentity
ciscoIkeFlowExtMIBConform=_CiscoIkeFlowExtMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,428,2))
_CifeMIBConformances_ObjectIdentity=ObjectIdentity
cifeMIBConformances=_CifeMIBConformances_ObjectIdentity((1,3,6,1,4,1,9,9,428,2,1))
_CifeMIBGroups_ObjectIdentity=ObjectIdentity
cifeMIBGroups=_CifeMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,428,2,2))
cifeGlobalsGroup=ObjectGroup((1,3,6,1,4,1,9,9,428,2,2,1))
cifeGlobalsGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:cifeGlobalsGroup.setStatus(_A)
cifeTunnelExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,428,2,2,2))
cifeTunnelExtGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:cifeTunnelExtGroup.setStatus(_A)
cifeMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,428,2,1,1))
cifeMIBCompliance.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:cifeMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoIkeFlowExtMIB':ciscoIkeFlowExtMIB,'ciscoIkeFlowExtMIBNotifs':ciscoIkeFlowExtMIBNotifs,'ciscoIkeFlowExtMIBObjects':ciscoIkeFlowExtMIBObjects,'cifeIkeGlobals':cifeIkeGlobals,_J:cifeClearAllTunnels,'cifeTunnelExtTable':cifeTunnelExtTable,'cifeTunnelExtEntry':cifeTunnelExtEntry,_I:cifeTunnelExtDoi,_K:cifeTunnelExtLocalIdenType,_L:cifeTunnelExtLocalIdentity,_M:cifeTunnelExtRemoteIdenType,_N:cifeTunnelExtRemoteIdentity,'ciscoIkeFlowExtMIBConform':ciscoIkeFlowExtMIBConform,'cifeMIBConformances':cifeMIBConformances,'cifeMIBCompliance':cifeMIBCompliance,'cifeMIBGroups':cifeMIBGroups,_O:cifeGlobalsGroup,_P:cifeTunnelExtGroup})