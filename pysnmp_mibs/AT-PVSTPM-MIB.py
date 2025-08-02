_H='pvstpmTxVlan'
_G='pvstpmRxVlan'
_F='pvstpmRxPort'
_E='pvstpmTopologyChangeVlan'
_D='pvstpmBridgeId'
_C='accessible-for-notify'
_B='AT-PVSTPM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
modules,=mibBuilder.importSymbols('AT-SMI-MIB','modules')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pvstpm=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,140))
if mibBuilder.loadTexts:pvstpm.setRevisions(('2006-03-29 16:51',))
_PvstpmEvents_ObjectIdentity=ObjectIdentity
pvstpmEvents=_PvstpmEvents_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,140,0))
_PvstpmEventVariables_ObjectIdentity=ObjectIdentity
pvstpmEventVariables=_PvstpmEventVariables_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,140,1))
_PvstpmBridgeId_Type=OctetString
_PvstpmBridgeId_Object=MibScalar
pvstpmBridgeId=_PvstpmBridgeId_Object((1,3,6,1,4,1,207,8,4,4,4,140,1,1),_PvstpmBridgeId_Type())
pvstpmBridgeId.setMaxAccess(_C)
if mibBuilder.loadTexts:pvstpmBridgeId.setStatus(_A)
_PvstpmTopologyChangeVlan_Type=VlanIndex
_PvstpmTopologyChangeVlan_Object=MibScalar
pvstpmTopologyChangeVlan=_PvstpmTopologyChangeVlan_Object((1,3,6,1,4,1,207,8,4,4,4,140,1,2),_PvstpmTopologyChangeVlan_Type())
pvstpmTopologyChangeVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:pvstpmTopologyChangeVlan.setStatus(_A)
_PvstpmRxPort_Type=Integer32
_PvstpmRxPort_Object=MibScalar
pvstpmRxPort=_PvstpmRxPort_Object((1,3,6,1,4,1,207,8,4,4,4,140,1,3),_PvstpmRxPort_Type())
pvstpmRxPort.setMaxAccess(_C)
if mibBuilder.loadTexts:pvstpmRxPort.setStatus(_A)
_PvstpmRxVlan_Type=VlanIndex
_PvstpmRxVlan_Object=MibScalar
pvstpmRxVlan=_PvstpmRxVlan_Object((1,3,6,1,4,1,207,8,4,4,4,140,1,4),_PvstpmRxVlan_Type())
pvstpmRxVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:pvstpmRxVlan.setStatus(_A)
_PvstpmTxVlan_Type=VlanIndex
_PvstpmTxVlan_Object=MibScalar
pvstpmTxVlan=_PvstpmTxVlan_Object((1,3,6,1,4,1,207,8,4,4,4,140,1,5),_PvstpmTxVlan_Type())
pvstpmTxVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:pvstpmTxVlan.setStatus(_A)
pvstpmTopologyChange=NotificationType((1,3,6,1,4,1,207,8,4,4,4,140,0,1))
pvstpmTopologyChange.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:pvstpmTopologyChange.setStatus(_A)
pvstpmInconsistentBPDU=NotificationType((1,3,6,1,4,1,207,8,4,4,4,140,0,2))
pvstpmInconsistentBPDU.setObjects(*((_B,_D),(_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:pvstpmInconsistentBPDU.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pvstpm':pvstpm,'pvstpmEvents':pvstpmEvents,'pvstpmTopologyChange':pvstpmTopologyChange,'pvstpmInconsistentBPDU':pvstpmInconsistentBPDU,'pvstpmEventVariables':pvstpmEventVariables,_D:pvstpmBridgeId,_E:pvstpmTopologyChangeVlan,_F:pvstpmRxPort,_G:pvstpmRxVlan,_H:pvstpmTxVlan})