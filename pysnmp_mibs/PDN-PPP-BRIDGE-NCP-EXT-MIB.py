_K='pdnPppBridgeExt802TaggedGroup'
_J='pdnPppBridgeExtStateMachineGroup'
_I='pdnPppBridgeRemoteToLocal802Tagged'
_H='pdnPppBridgeLocalToRemote802Tagged'
_G='pdnPppBridgeMediaIeee802Tagged'
_F='pdnPppBridgeBcpLinkStatusCurrState'
_E='pdnPppBridgeMediaConfigExtEntry'
_D='pdnPppBridgeExtEntry'
_C='read-only'
_B='PDN-PPP-BRIDGE-NCP-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pdn_interfaces,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-interfaces')
PdnPPPState,SwitchState=mibBuilder.importSymbols('PDN-TC','PdnPPPState','SwitchState')
pppBridgeEntry,pppBridgeMediaConfigEntry=mibBuilder.importSymbols('PPP-BRIDGE-NCP-MIB','pppBridgeEntry','pppBridgeMediaConfigEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnPppBridgeExtMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,6,29))
if mibBuilder.loadTexts:pdnPppBridgeExtMIB.setRevisions(('2004-09-10 00:00',))
_PdnPppBridgeExtNotifications_ObjectIdentity=ObjectIdentity
pdnPppBridgeExtNotifications=_PdnPppBridgeExtNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,29,0))
_PdnPppBridgeExtObjects_ObjectIdentity=ObjectIdentity
pdnPppBridgeExtObjects=_PdnPppBridgeExtObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,29,1))
_PdnPppBridgeExtTable_Object=MibTable
pdnPppBridgeExtTable=_PdnPppBridgeExtTable_Object((1,3,6,1,4,1,1795,2,24,2,6,29,1,1))
if mibBuilder.loadTexts:pdnPppBridgeExtTable.setStatus(_A)
_PdnPppBridgeExtEntry_Object=MibTableRow
pdnPppBridgeExtEntry=_PdnPppBridgeExtEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,29,1,1,1))
if mibBuilder.loadTexts:pdnPppBridgeExtEntry.setStatus(_A)
_PdnPppBridgeBcpLinkStatusCurrState_Type=PdnPPPState
_PdnPppBridgeBcpLinkStatusCurrState_Object=MibTableColumn
pdnPppBridgeBcpLinkStatusCurrState=_PdnPppBridgeBcpLinkStatusCurrState_Object((1,3,6,1,4,1,1795,2,24,2,6,29,1,1,1,1),_PdnPppBridgeBcpLinkStatusCurrState_Type())
pdnPppBridgeBcpLinkStatusCurrState.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppBridgeBcpLinkStatusCurrState.setStatus(_A)
_PdnPppBridgeLocalToRemote802Tagged_Type=SwitchState
_PdnPppBridgeLocalToRemote802Tagged_Object=MibTableColumn
pdnPppBridgeLocalToRemote802Tagged=_PdnPppBridgeLocalToRemote802Tagged_Object((1,3,6,1,4,1,1795,2,24,2,6,29,1,1,1,2),_PdnPppBridgeLocalToRemote802Tagged_Type())
pdnPppBridgeLocalToRemote802Tagged.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppBridgeLocalToRemote802Tagged.setStatus(_A)
_PdnPppBridgeRemoteToLocal802Tagged_Type=SwitchState
_PdnPppBridgeRemoteToLocal802Tagged_Object=MibTableColumn
pdnPppBridgeRemoteToLocal802Tagged=_PdnPppBridgeRemoteToLocal802Tagged_Object((1,3,6,1,4,1,1795,2,24,2,6,29,1,1,1,3),_PdnPppBridgeRemoteToLocal802Tagged_Type())
pdnPppBridgeRemoteToLocal802Tagged.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppBridgeRemoteToLocal802Tagged.setStatus(_A)
_PdnPppBridgeMediaConfigExtTable_Object=MibTable
pdnPppBridgeMediaConfigExtTable=_PdnPppBridgeMediaConfigExtTable_Object((1,3,6,1,4,1,1795,2,24,2,6,29,1,2))
if mibBuilder.loadTexts:pdnPppBridgeMediaConfigExtTable.setStatus(_A)
_PdnPppBridgeMediaConfigExtEntry_Object=MibTableRow
pdnPppBridgeMediaConfigExtEntry=_PdnPppBridgeMediaConfigExtEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,29,1,2,1))
if mibBuilder.loadTexts:pdnPppBridgeMediaConfigExtEntry.setStatus(_A)
_PdnPppBridgeMediaIeee802Tagged_Type=SwitchState
_PdnPppBridgeMediaIeee802Tagged_Object=MibTableColumn
pdnPppBridgeMediaIeee802Tagged=_PdnPppBridgeMediaIeee802Tagged_Object((1,3,6,1,4,1,1795,2,24,2,6,29,1,2,1,1),_PdnPppBridgeMediaIeee802Tagged_Type())
pdnPppBridgeMediaIeee802Tagged.setMaxAccess('read-write')
if mibBuilder.loadTexts:pdnPppBridgeMediaIeee802Tagged.setStatus(_A)
_PdnPppBridgeExtAFNs_ObjectIdentity=ObjectIdentity
pdnPppBridgeExtAFNs=_PdnPppBridgeExtAFNs_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,29,2))
_PdnPppBridgeExtConformance_ObjectIdentity=ObjectIdentity
pdnPppBridgeExtConformance=_PdnPppBridgeExtConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,29,3))
_PdnPppBridgeExtCompliances_ObjectIdentity=ObjectIdentity
pdnPppBridgeExtCompliances=_PdnPppBridgeExtCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,29,3,1))
_PdnPppBridgeExtGroups_ObjectIdentity=ObjectIdentity
pdnPppBridgeExtGroups=_PdnPppBridgeExtGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,29,3,2))
_PdnPppBridgeExtObjGroups_ObjectIdentity=ObjectIdentity
pdnPppBridgeExtObjGroups=_PdnPppBridgeExtObjGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,29,3,2,1))
_PdnPppBridgeExtAfnGroups_ObjectIdentity=ObjectIdentity
pdnPppBridgeExtAfnGroups=_PdnPppBridgeExtAfnGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,29,3,2,2))
_PdnPppBridgeExtNtfyGroups_ObjectIdentity=ObjectIdentity
pdnPppBridgeExtNtfyGroups=_PdnPppBridgeExtNtfyGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,29,3,2,3))
pppBridgeEntry.registerAugmentions((_B,_D))
pdnPppBridgeExtEntry.setIndexNames(*pppBridgeEntry.getIndexNames())
pppBridgeMediaConfigEntry.registerAugmentions((_B,_E))
pdnPppBridgeMediaConfigExtEntry.setIndexNames(*pppBridgeMediaConfigEntry.getIndexNames())
pdnPppBridgeExtStateMachineGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,29,3,2,1,1))
pdnPppBridgeExtStateMachineGroup.setObjects((_B,_F))
if mibBuilder.loadTexts:pdnPppBridgeExtStateMachineGroup.setStatus(_A)
pdnPppBridgeExt802TaggedGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,29,3,2,1,2))
pdnPppBridgeExt802TaggedGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:pdnPppBridgeExt802TaggedGroup.setStatus(_A)
pdnPppBridgeExtCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,6,29,3,1,1))
pdnPppBridgeExtCompliance.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:pdnPppBridgeExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pdnPppBridgeExtMIB':pdnPppBridgeExtMIB,'pdnPppBridgeExtNotifications':pdnPppBridgeExtNotifications,'pdnPppBridgeExtObjects':pdnPppBridgeExtObjects,'pdnPppBridgeExtTable':pdnPppBridgeExtTable,_D:pdnPppBridgeExtEntry,_F:pdnPppBridgeBcpLinkStatusCurrState,_H:pdnPppBridgeLocalToRemote802Tagged,_I:pdnPppBridgeRemoteToLocal802Tagged,'pdnPppBridgeMediaConfigExtTable':pdnPppBridgeMediaConfigExtTable,_E:pdnPppBridgeMediaConfigExtEntry,_G:pdnPppBridgeMediaIeee802Tagged,'pdnPppBridgeExtAFNs':pdnPppBridgeExtAFNs,'pdnPppBridgeExtConformance':pdnPppBridgeExtConformance,'pdnPppBridgeExtCompliances':pdnPppBridgeExtCompliances,'pdnPppBridgeExtCompliance':pdnPppBridgeExtCompliance,'pdnPppBridgeExtGroups':pdnPppBridgeExtGroups,'pdnPppBridgeExtObjGroups':pdnPppBridgeExtObjGroups,_J:pdnPppBridgeExtStateMachineGroup,_K:pdnPppBridgeExt802TaggedGroup,'pdnPppBridgeExtAfnGroups':pdnPppBridgeExtAfnGroups,'pdnPppBridgeExtNtfyGroups':pdnPppBridgeExtNtfyGroups})