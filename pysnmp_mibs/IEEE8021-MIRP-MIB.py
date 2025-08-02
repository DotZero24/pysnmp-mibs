_Q='ieee8021MirpV2ReqdGroup'
_P='ieee8021PbbMirpPnpPortNumber'
_O='ieee8021PbbMirpPnpEnable'
_N='ieee8021PbbMirpDestSelector'
_M='ieee8021PbbMirpBvid'
_L='ieee8021PbbMirpEnableStatus'
_K='ieee8021MirpV2PortEnabledStatus'
_J='ieee8021MirpV2PortEntry'
_I='Integer32'
_H='systemGroup'
_G='SNMPv2-MIB'
_F='VlanIdOrNone'
_E='IEEE8021BridgePortNumberOrZero'
_D='read-write'
_C='TruthValue'
_B='IEEE8021-MIRP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ieee8021BridgeBasePortEntry,=mibBuilder.importSymbols('IEEE8021-BRIDGE-MIB','ieee8021BridgeBasePortEntry')
ieee8021PbbBackboneEdgeBridgeObjects,=mibBuilder.importSymbols('IEEE8021-PBB-MIB','ieee8021PbbBackboneEdgeBridgeObjects')
IEEE8021BridgePortNumberOrZero,=mibBuilder.importSymbols('IEEE8021-TC-MIB',_E)
VlanIdOrNone,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
systemGroup,=mibBuilder.importSymbols(_G,_H)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_C)
ieee8021MirpMib=ModuleIdentity((1,3,111,2,802,1,1,23))
if mibBuilder.loadTexts:ieee8021MirpMib.setRevisions(('2018-06-28 00:00','2014-12-15 00:00','2011-04-05 00:00'))
class _Ieee8021PbbMirpEnableStatus_Type(TruthValue):defaultValue=2
_Ieee8021PbbMirpEnableStatus_Type.__name__=_C
_Ieee8021PbbMirpEnableStatus_Object=MibScalar
ieee8021PbbMirpEnableStatus=_Ieee8021PbbMirpEnableStatus_Object((1,3,111,2,802,1,1,9,1,1,1,7),_Ieee8021PbbMirpEnableStatus_Type())
ieee8021PbbMirpEnableStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021PbbMirpEnableStatus.setStatus(_A)
class _Ieee8021PbbMirpBvid_Type(VlanIdOrNone):defaultValue=0
_Ieee8021PbbMirpBvid_Type.__name__=_F
_Ieee8021PbbMirpBvid_Object=MibScalar
ieee8021PbbMirpBvid=_Ieee8021PbbMirpBvid_Object((1,3,111,2,802,1,1,9,1,1,1,8),_Ieee8021PbbMirpBvid_Type())
ieee8021PbbMirpBvid.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021PbbMirpBvid.setStatus(_A)
class _Ieee8021PbbMirpDestSelector_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cbpMirpGroup',1),('cbpMirpVlan',2),('cbpMirpTable',3)))
_Ieee8021PbbMirpDestSelector_Type.__name__=_I
_Ieee8021PbbMirpDestSelector_Object=MibScalar
ieee8021PbbMirpDestSelector=_Ieee8021PbbMirpDestSelector_Object((1,3,111,2,802,1,1,9,1,1,1,9),_Ieee8021PbbMirpDestSelector_Type())
ieee8021PbbMirpDestSelector.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021PbbMirpDestSelector.setStatus(_A)
class _Ieee8021PbbMirpPnpEnable_Type(TruthValue):defaultValue=1
_Ieee8021PbbMirpPnpEnable_Type.__name__=_C
_Ieee8021PbbMirpPnpEnable_Object=MibScalar
ieee8021PbbMirpPnpEnable=_Ieee8021PbbMirpPnpEnable_Object((1,3,111,2,802,1,1,9,1,1,1,10),_Ieee8021PbbMirpPnpEnable_Type())
ieee8021PbbMirpPnpEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021PbbMirpPnpEnable.setStatus(_A)
class _Ieee8021PbbMirpPnpPortNumber_Type(IEEE8021BridgePortNumberOrZero):defaultValue=0
_Ieee8021PbbMirpPnpPortNumber_Type.__name__=_E
_Ieee8021PbbMirpPnpPortNumber_Object=MibScalar
ieee8021PbbMirpPnpPortNumber=_Ieee8021PbbMirpPnpPortNumber_Object((1,3,111,2,802,1,1,9,1,1,1,11),_Ieee8021PbbMirpPnpPortNumber_Type())
ieee8021PbbMirpPnpPortNumber.setMaxAccess('read-only')
if mibBuilder.loadTexts:ieee8021PbbMirpPnpPortNumber.setStatus(_A)
_Ieee8021MirpV2MIBObjects_ObjectIdentity=ObjectIdentity
ieee8021MirpV2MIBObjects=_Ieee8021MirpV2MIBObjects_ObjectIdentity((1,3,111,2,802,1,1,23,1))
_Ieee8021MirpV2PortTable_Object=MibTable
ieee8021MirpV2PortTable=_Ieee8021MirpV2PortTable_Object((1,3,111,2,802,1,1,23,1,1))
if mibBuilder.loadTexts:ieee8021MirpV2PortTable.setStatus(_A)
_Ieee8021MirpV2PortEntry_Object=MibTableRow
ieee8021MirpV2PortEntry=_Ieee8021MirpV2PortEntry_Object((1,3,111,2,802,1,1,23,1,1,1))
if mibBuilder.loadTexts:ieee8021MirpV2PortEntry.setStatus(_A)
class _Ieee8021MirpV2PortEnabledStatus_Type(TruthValue):defaultValue=1
_Ieee8021MirpV2PortEnabledStatus_Type.__name__=_C
_Ieee8021MirpV2PortEnabledStatus_Object=MibTableColumn
ieee8021MirpV2PortEnabledStatus=_Ieee8021MirpV2PortEnabledStatus_Object((1,3,111,2,802,1,1,23,1,1,1,1),_Ieee8021MirpV2PortEnabledStatus_Type())
ieee8021MirpV2PortEnabledStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:ieee8021MirpV2PortEnabledStatus.setStatus(_A)
_Ieee8021MirpV2Conformance_ObjectIdentity=ObjectIdentity
ieee8021MirpV2Conformance=_Ieee8021MirpV2Conformance_ObjectIdentity((1,3,111,2,802,1,1,23,2))
_Ieee8021MirpV2Compliances_ObjectIdentity=ObjectIdentity
ieee8021MirpV2Compliances=_Ieee8021MirpV2Compliances_ObjectIdentity((1,3,111,2,802,1,1,23,2,1))
_Ieee8021MirpV2Groups_ObjectIdentity=ObjectIdentity
ieee8021MirpV2Groups=_Ieee8021MirpV2Groups_ObjectIdentity((1,3,111,2,802,1,1,23,2,2))
ieee8021BridgeBasePortEntry.registerAugmentions((_B,_J))
ieee8021MirpV2PortEntry.setIndexNames(*ieee8021BridgeBasePortEntry.getIndexNames())
ieee8021MirpV2ReqdGroup=ObjectGroup((1,3,111,2,802,1,1,23,2,2,1))
ieee8021MirpV2ReqdGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:ieee8021MirpV2ReqdGroup.setStatus(_A)
ieee8021MirpV2BridgeCompliance=ModuleCompliance((1,3,111,2,802,1,1,23,2,1,1))
ieee8021MirpV2BridgeCompliance.setObjects(*((_G,_H),(_B,_Q)))
if mibBuilder.loadTexts:ieee8021MirpV2BridgeCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_L:ieee8021PbbMirpEnableStatus,_M:ieee8021PbbMirpBvid,_N:ieee8021PbbMirpDestSelector,_O:ieee8021PbbMirpPnpEnable,_P:ieee8021PbbMirpPnpPortNumber,'ieee8021MirpMib':ieee8021MirpMib,'ieee8021MirpV2MIBObjects':ieee8021MirpV2MIBObjects,'ieee8021MirpV2PortTable':ieee8021MirpV2PortTable,_J:ieee8021MirpV2PortEntry,_K:ieee8021MirpV2PortEnabledStatus,'ieee8021MirpV2Conformance':ieee8021MirpV2Conformance,'ieee8021MirpV2Compliances':ieee8021MirpV2Compliances,'ieee8021MirpV2BridgeCompliance':ieee8021MirpV2BridgeCompliance,'ieee8021MirpV2Groups':ieee8021MirpV2Groups,_Q:ieee8021MirpV2ReqdGroup})