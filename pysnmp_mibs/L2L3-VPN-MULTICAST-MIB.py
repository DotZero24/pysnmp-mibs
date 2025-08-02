_N='l2L3VpnMcastOptionalGroup'
_M='l2L3VpnMcastPmsiTunnelIf'
_L='l2L3VpnMcastPmsiTunnelPointer'
_K='l2L3VpnMcastPmsiTunnelAttributeMplsLabel'
_J='l2L3VpnMCastPmsiTunnelLeafInfoRequired'
_I='not-accessible'
_H='l2L3VpnMcastPmsiTunnelAttributeId'
_G='l2L3VpnMcastPmsiTunnelAttributeType'
_F='Integer32'
_E='l2L3VpnMcastCoreGroup'
_D='RowPointer'
_C='read-only'
_B='L2L3-VPN-MULTICAST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
L2L3VpnMcastProviderTunnelId,L2L3VpnMcastProviderTunnelType=mibBuilder.importSymbols('L2L3-VPN-MULTICAST-TC-MIB','L2L3VpnMcastProviderTunnelId','L2L3VpnMcastProviderTunnelType')
MplsLabel,=mibBuilder.importSymbols('MPLS-TC-STD-MIB','MplsLabel')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2','zeroDotZero')
DisplayString,PhysAddress,RowPointer,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress',_D,'TextualConvention')
l2L3VpnMcastMIB=ModuleIdentity((1,3,6,1,2,1,245))
if mibBuilder.loadTexts:l2L3VpnMcastMIB.setRevisions(('2018-12-14 00:00',))
_L2L3VpnMcastStates_ObjectIdentity=ObjectIdentity
l2L3VpnMcastStates=_L2L3VpnMcastStates_ObjectIdentity((1,3,6,1,2,1,245,1))
_L2L3VpnMcastPmsiTunnelAttributeTable_Object=MibTable
l2L3VpnMcastPmsiTunnelAttributeTable=_L2L3VpnMcastPmsiTunnelAttributeTable_Object((1,3,6,1,2,1,245,1,1))
if mibBuilder.loadTexts:l2L3VpnMcastPmsiTunnelAttributeTable.setStatus(_A)
_L2L3VpnMcastPmsiTunnelAttributeEntry_Object=MibTableRow
l2L3VpnMcastPmsiTunnelAttributeEntry=_L2L3VpnMcastPmsiTunnelAttributeEntry_Object((1,3,6,1,2,1,245,1,1,1))
l2L3VpnMcastPmsiTunnelAttributeEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:l2L3VpnMcastPmsiTunnelAttributeEntry.setStatus(_A)
_L2L3VpnMcastPmsiTunnelAttributeType_Type=L2L3VpnMcastProviderTunnelType
_L2L3VpnMcastPmsiTunnelAttributeType_Object=MibTableColumn
l2L3VpnMcastPmsiTunnelAttributeType=_L2L3VpnMcastPmsiTunnelAttributeType_Object((1,3,6,1,2,1,245,1,1,1,1),_L2L3VpnMcastPmsiTunnelAttributeType_Type())
l2L3VpnMcastPmsiTunnelAttributeType.setMaxAccess(_I)
if mibBuilder.loadTexts:l2L3VpnMcastPmsiTunnelAttributeType.setStatus(_A)
_L2L3VpnMcastPmsiTunnelAttributeId_Type=L2L3VpnMcastProviderTunnelId
_L2L3VpnMcastPmsiTunnelAttributeId_Object=MibTableColumn
l2L3VpnMcastPmsiTunnelAttributeId=_L2L3VpnMcastPmsiTunnelAttributeId_Object((1,3,6,1,2,1,245,1,1,1,2),_L2L3VpnMcastPmsiTunnelAttributeId_Type())
l2L3VpnMcastPmsiTunnelAttributeId.setMaxAccess(_I)
if mibBuilder.loadTexts:l2L3VpnMcastPmsiTunnelAttributeId.setStatus(_A)
class _L2L3VpnMCastPmsiTunnelLeafInfoRequired_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('false',0),('true',1),('notAvailable',2)))
_L2L3VpnMCastPmsiTunnelLeafInfoRequired_Type.__name__=_F
_L2L3VpnMCastPmsiTunnelLeafInfoRequired_Object=MibTableColumn
l2L3VpnMCastPmsiTunnelLeafInfoRequired=_L2L3VpnMCastPmsiTunnelLeafInfoRequired_Object((1,3,6,1,2,1,245,1,1,1,3),_L2L3VpnMCastPmsiTunnelLeafInfoRequired_Type())
l2L3VpnMCastPmsiTunnelLeafInfoRequired.setMaxAccess(_C)
if mibBuilder.loadTexts:l2L3VpnMCastPmsiTunnelLeafInfoRequired.setStatus(_A)
_L2L3VpnMcastPmsiTunnelAttributeMplsLabel_Type=MplsLabel
_L2L3VpnMcastPmsiTunnelAttributeMplsLabel_Object=MibTableColumn
l2L3VpnMcastPmsiTunnelAttributeMplsLabel=_L2L3VpnMcastPmsiTunnelAttributeMplsLabel_Object((1,3,6,1,2,1,245,1,1,1,4),_L2L3VpnMcastPmsiTunnelAttributeMplsLabel_Type())
l2L3VpnMcastPmsiTunnelAttributeMplsLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:l2L3VpnMcastPmsiTunnelAttributeMplsLabel.setStatus(_A)
class _L2L3VpnMcastPmsiTunnelPointer_Type(RowPointer):defaultValue=0,0
_L2L3VpnMcastPmsiTunnelPointer_Type.__name__=_D
_L2L3VpnMcastPmsiTunnelPointer_Object=MibTableColumn
l2L3VpnMcastPmsiTunnelPointer=_L2L3VpnMcastPmsiTunnelPointer_Object((1,3,6,1,2,1,245,1,1,1,5),_L2L3VpnMcastPmsiTunnelPointer_Type())
l2L3VpnMcastPmsiTunnelPointer.setMaxAccess(_C)
if mibBuilder.loadTexts:l2L3VpnMcastPmsiTunnelPointer.setStatus(_A)
class _L2L3VpnMcastPmsiTunnelIf_Type(RowPointer):defaultValue=0,0
_L2L3VpnMcastPmsiTunnelIf_Type.__name__=_D
_L2L3VpnMcastPmsiTunnelIf_Object=MibTableColumn
l2L3VpnMcastPmsiTunnelIf=_L2L3VpnMcastPmsiTunnelIf_Object((1,3,6,1,2,1,245,1,1,1,6),_L2L3VpnMcastPmsiTunnelIf_Type())
l2L3VpnMcastPmsiTunnelIf.setMaxAccess(_C)
if mibBuilder.loadTexts:l2L3VpnMcastPmsiTunnelIf.setStatus(_A)
_L2L3VpnMcastConformance_ObjectIdentity=ObjectIdentity
l2L3VpnMcastConformance=_L2L3VpnMcastConformance_ObjectIdentity((1,3,6,1,2,1,245,2))
_L2L3VpnMcastCompliances_ObjectIdentity=ObjectIdentity
l2L3VpnMcastCompliances=_L2L3VpnMcastCompliances_ObjectIdentity((1,3,6,1,2,1,245,2,1))
_L2L3VpnMcastGroups_ObjectIdentity=ObjectIdentity
l2L3VpnMcastGroups=_L2L3VpnMcastGroups_ObjectIdentity((1,3,6,1,2,1,245,2,2))
l2L3VpnMcastCoreGroup=ObjectGroup((1,3,6,1,2,1,245,2,2,1))
l2L3VpnMcastCoreGroup.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:l2L3VpnMcastCoreGroup.setStatus(_A)
l2L3VpnMcastOptionalGroup=ObjectGroup((1,3,6,1,2,1,245,2,2,2))
l2L3VpnMcastOptionalGroup.setObjects(*((_B,_L),(_B,_M)))
if mibBuilder.loadTexts:l2L3VpnMcastOptionalGroup.setStatus(_A)
l2L3VpnMcastCoreCompliance=ModuleCompliance((1,3,6,1,2,1,245,2,1,1))
l2L3VpnMcastCoreCompliance.setObjects((_B,_E))
if mibBuilder.loadTexts:l2L3VpnMcastCoreCompliance.setStatus(_A)
l2L3VpnMcastFullCompliance=ModuleCompliance((1,3,6,1,2,1,245,2,1,2))
l2L3VpnMcastFullCompliance.setObjects(*((_B,_E),(_B,_N)))
if mibBuilder.loadTexts:l2L3VpnMcastFullCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'l2L3VpnMcastMIB':l2L3VpnMcastMIB,'l2L3VpnMcastStates':l2L3VpnMcastStates,'l2L3VpnMcastPmsiTunnelAttributeTable':l2L3VpnMcastPmsiTunnelAttributeTable,'l2L3VpnMcastPmsiTunnelAttributeEntry':l2L3VpnMcastPmsiTunnelAttributeEntry,_G:l2L3VpnMcastPmsiTunnelAttributeType,_H:l2L3VpnMcastPmsiTunnelAttributeId,_J:l2L3VpnMCastPmsiTunnelLeafInfoRequired,_K:l2L3VpnMcastPmsiTunnelAttributeMplsLabel,_L:l2L3VpnMcastPmsiTunnelPointer,_M:l2L3VpnMcastPmsiTunnelIf,'l2L3VpnMcastConformance':l2L3VpnMcastConformance,'l2L3VpnMcastCompliances':l2L3VpnMcastCompliances,'l2L3VpnMcastCoreCompliance':l2L3VpnMcastCoreCompliance,'l2L3VpnMcastFullCompliance':l2L3VpnMcastFullCompliance,'l2L3VpnMcastGroups':l2L3VpnMcastGroups,_E:l2L3VpnMcastCoreGroup,_N:l2L3VpnMcastOptionalGroup})