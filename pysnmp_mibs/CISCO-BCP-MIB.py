_Z='cBcpMIBGroup'
_Y='bcpConfigBCPacketIndicator'
_X='bcpConfigMgmtInline'
_W='bcpConfigIeee802dot1qTagged'
_V='bcpConfigSpanTree'
_U='bcpConfigSpanTreeControl'
_T='bcpConfigMacAddress'
_S='bcpConfigMacAddressControl'
_R='bcpConfigTinygram'
_Q='bcpConfigMacType'
_P='bcpConfigMacSupport'
_O='bcpConfigLineId'
_N='bcpConfigLineIdControl'
_M='bcpConfigBridgeId'
_L='bcpConfigBridgeIdControl'
_K='bcpOperStatus'
_J='DisplayString'
_I='Unsigned32'
_H='ifIndex'
_G='IF-MIB'
_F='disabled'
_E='enabled'
_D='Integer32'
_C='read-write'
_B='CISCO-BCP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
ciscoBcpMIB=ModuleIdentity((1,3,6,1,4,1,9,9,275))
if mibBuilder.loadTexts:ciscoBcpMIB.setRevisions(('2004-08-31 00:00','2002-08-02 00:00'))
_CiscoBcpMIBObjects_ObjectIdentity=ObjectIdentity
ciscoBcpMIBObjects=_CiscoBcpMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,275,1))
_BcpOperTable_Object=MibTable
bcpOperTable=_BcpOperTable_Object((1,3,6,1,4,1,9,9,275,1,1))
if mibBuilder.loadTexts:bcpOperTable.setStatus(_A)
_BcpOperEntry_Object=MibTableRow
bcpOperEntry=_BcpOperEntry_Object((1,3,6,1,4,1,9,9,275,1,1,1))
bcpOperEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:bcpOperEntry.setStatus(_A)
class _BcpOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('open',1),('closed',2),('listening',3)))
_BcpOperStatus_Type.__name__=_D
_BcpOperStatus_Object=MibTableColumn
bcpOperStatus=_BcpOperStatus_Object((1,3,6,1,4,1,9,9,275,1,1,1,1),_BcpOperStatus_Type())
bcpOperStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:bcpOperStatus.setStatus(_A)
_BcpConfigTable_Object=MibTable
bcpConfigTable=_BcpConfigTable_Object((1,3,6,1,4,1,9,9,275,1,2))
if mibBuilder.loadTexts:bcpConfigTable.setStatus(_A)
_BcpConfigEntry_Object=MibTableRow
bcpConfigEntry=_BcpConfigEntry_Object((1,3,6,1,4,1,9,9,275,1,2,1))
bcpConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:bcpConfigEntry.setStatus(_A)
class _BcpConfigBridgeIdControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BcpConfigBridgeIdControl_Type.__name__=_D
_BcpConfigBridgeIdControl_Object=MibTableColumn
bcpConfigBridgeIdControl=_BcpConfigBridgeIdControl_Object((1,3,6,1,4,1,9,9,275,1,2,1,1),_BcpConfigBridgeIdControl_Type())
bcpConfigBridgeIdControl.setMaxAccess(_C)
if mibBuilder.loadTexts:bcpConfigBridgeIdControl.setStatus(_A)
class _BcpConfigBridgeId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_BcpConfigBridgeId_Type.__name__=_I
_BcpConfigBridgeId_Object=MibTableColumn
bcpConfigBridgeId=_BcpConfigBridgeId_Object((1,3,6,1,4,1,9,9,275,1,2,1,2),_BcpConfigBridgeId_Type())
bcpConfigBridgeId.setMaxAccess(_C)
if mibBuilder.loadTexts:bcpConfigBridgeId.setStatus(_A)
class _BcpConfigLineIdControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BcpConfigLineIdControl_Type.__name__=_D
_BcpConfigLineIdControl_Object=MibTableColumn
bcpConfigLineIdControl=_BcpConfigLineIdControl_Object((1,3,6,1,4,1,9,9,275,1,2,1,3),_BcpConfigLineIdControl_Type())
bcpConfigLineIdControl.setMaxAccess(_C)
if mibBuilder.loadTexts:bcpConfigLineIdControl.setStatus(_A)
class _BcpConfigLineId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_BcpConfigLineId_Type.__name__=_I
_BcpConfigLineId_Object=MibTableColumn
bcpConfigLineId=_BcpConfigLineId_Object((1,3,6,1,4,1,9,9,275,1,2,1,4),_BcpConfigLineId_Type())
bcpConfigLineId.setMaxAccess(_C)
if mibBuilder.loadTexts:bcpConfigLineId.setStatus(_A)
class _BcpConfigMacSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BcpConfigMacSupport_Type.__name__=_D
_BcpConfigMacSupport_Object=MibTableColumn
bcpConfigMacSupport=_BcpConfigMacSupport_Object((1,3,6,1,4,1,9,9,275,1,2,1,5),_BcpConfigMacSupport_Type())
bcpConfigMacSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:bcpConfigMacSupport.setStatus(_A)
class _BcpConfigMacType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,11,12)));namedValues=NamedValues(*(('ieee802dot3Canonical',1),('ieee802dot4Canonical',2),('ieee802dot5NonCanonical',3),('fddiNonCanonical',4),('ieee802dot5Canonical',11),('fddiCanonical',12)))
_BcpConfigMacType_Type.__name__=_D
_BcpConfigMacType_Object=MibTableColumn
bcpConfigMacType=_BcpConfigMacType_Object((1,3,6,1,4,1,9,9,275,1,2,1,6),_BcpConfigMacType_Type())
bcpConfigMacType.setMaxAccess(_C)
if mibBuilder.loadTexts:bcpConfigMacType.setStatus(_A)
class _BcpConfigTinygram_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BcpConfigTinygram_Type.__name__=_D
_BcpConfigTinygram_Object=MibTableColumn
bcpConfigTinygram=_BcpConfigTinygram_Object((1,3,6,1,4,1,9,9,275,1,2,1,7),_BcpConfigTinygram_Type())
bcpConfigTinygram.setMaxAccess(_C)
if mibBuilder.loadTexts:bcpConfigTinygram.setStatus(_A)
class _BcpConfigMacAddressControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BcpConfigMacAddressControl_Type.__name__=_D
_BcpConfigMacAddressControl_Object=MibTableColumn
bcpConfigMacAddressControl=_BcpConfigMacAddressControl_Object((1,3,6,1,4,1,9,9,275,1,2,1,8),_BcpConfigMacAddressControl_Type())
bcpConfigMacAddressControl.setMaxAccess(_C)
if mibBuilder.loadTexts:bcpConfigMacAddressControl.setStatus(_A)
class _BcpConfigMacAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_BcpConfigMacAddress_Type.__name__=_J
_BcpConfigMacAddress_Object=MibTableColumn
bcpConfigMacAddress=_BcpConfigMacAddress_Object((1,3,6,1,4,1,9,9,275,1,2,1,9),_BcpConfigMacAddress_Type())
bcpConfigMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bcpConfigMacAddress.setStatus(_A)
class _BcpConfigSpanTreeControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BcpConfigSpanTreeControl_Type.__name__=_D
_BcpConfigSpanTreeControl_Object=MibTableColumn
bcpConfigSpanTreeControl=_BcpConfigSpanTreeControl_Object((1,3,6,1,4,1,9,9,275,1,2,1,10),_BcpConfigSpanTreeControl_Type())
bcpConfigSpanTreeControl.setMaxAccess(_C)
if mibBuilder.loadTexts:bcpConfigSpanTreeControl.setStatus(_A)
class _BcpConfigSpanTree_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('null',0),('ieee802dot1D',1),('ieee802dot1GExtended',2),('ibmSourceRoute',3),('decLanBridge100',4)))
_BcpConfigSpanTree_Type.__name__=_D
_BcpConfigSpanTree_Object=MibTableColumn
bcpConfigSpanTree=_BcpConfigSpanTree_Object((1,3,6,1,4,1,9,9,275,1,2,1,11),_BcpConfigSpanTree_Type())
bcpConfigSpanTree.setMaxAccess(_C)
if mibBuilder.loadTexts:bcpConfigSpanTree.setStatus(_A)
class _BcpConfigIeee802dot1qTagged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BcpConfigIeee802dot1qTagged_Type.__name__=_D
_BcpConfigIeee802dot1qTagged_Object=MibTableColumn
bcpConfigIeee802dot1qTagged=_BcpConfigIeee802dot1qTagged_Object((1,3,6,1,4,1,9,9,275,1,2,1,12),_BcpConfigIeee802dot1qTagged_Type())
bcpConfigIeee802dot1qTagged.setMaxAccess(_C)
if mibBuilder.loadTexts:bcpConfigIeee802dot1qTagged.setStatus(_A)
class _BcpConfigMgmtInline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BcpConfigMgmtInline_Type.__name__=_D
_BcpConfigMgmtInline_Object=MibTableColumn
bcpConfigMgmtInline=_BcpConfigMgmtInline_Object((1,3,6,1,4,1,9,9,275,1,2,1,13),_BcpConfigMgmtInline_Type())
bcpConfigMgmtInline.setMaxAccess(_C)
if mibBuilder.loadTexts:bcpConfigMgmtInline.setStatus(_A)
class _BcpConfigBCPacketIndicator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BcpConfigBCPacketIndicator_Type.__name__=_D
_BcpConfigBCPacketIndicator_Object=MibTableColumn
bcpConfigBCPacketIndicator=_BcpConfigBCPacketIndicator_Object((1,3,6,1,4,1,9,9,275,1,2,1,14),_BcpConfigBCPacketIndicator_Type())
bcpConfigBCPacketIndicator.setMaxAccess(_C)
if mibBuilder.loadTexts:bcpConfigBCPacketIndicator.setStatus(_A)
_CBcpMIBConformance_ObjectIdentity=ObjectIdentity
cBcpMIBConformance=_CBcpMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,275,3))
_CBcpMIBCompliances_ObjectIdentity=ObjectIdentity
cBcpMIBCompliances=_CBcpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,275,3,1))
_CBcpMIBGroups_ObjectIdentity=ObjectIdentity
cBcpMIBGroups=_CBcpMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,275,3,2))
cBcpMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,275,3,2,1))
cBcpMIBGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:cBcpMIBGroup.setStatus(_A)
cBcpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,275,3,1,1))
cBcpMIBCompliance.setObjects((_B,_Z))
if mibBuilder.loadTexts:cBcpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoBcpMIB':ciscoBcpMIB,'ciscoBcpMIBObjects':ciscoBcpMIBObjects,'bcpOperTable':bcpOperTable,'bcpOperEntry':bcpOperEntry,_K:bcpOperStatus,'bcpConfigTable':bcpConfigTable,'bcpConfigEntry':bcpConfigEntry,_L:bcpConfigBridgeIdControl,_M:bcpConfigBridgeId,_N:bcpConfigLineIdControl,_O:bcpConfigLineId,_P:bcpConfigMacSupport,_Q:bcpConfigMacType,_R:bcpConfigTinygram,_S:bcpConfigMacAddressControl,_T:bcpConfigMacAddress,_U:bcpConfigSpanTreeControl,_V:bcpConfigSpanTree,_W:bcpConfigIeee802dot1qTagged,_X:bcpConfigMgmtInline,_Y:bcpConfigBCPacketIndicator,'cBcpMIBConformance':cBcpMIBConformance,'cBcpMIBCompliances':cBcpMIBCompliances,'cBcpMIBCompliance':cBcpMIBCompliance,'cBcpMIBGroups':cBcpMIBGroups,_Z:cBcpMIBGroup})