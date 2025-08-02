_U='brcdSPXPEGroupCBSPXPort'
_T='brcdSPXCBSPXLagPrimaryPort'
_S='create'
_R='brcdSPXCBSPXPortPort'
_Q='brcdSPXOperUnitIndex'
_P='reserved'
_O='remote'
_N='brcdSPXConfigUnitIndex'
_M='disabled'
_L='delete'
_K='valid'
_J='other'
_I='enabled'
_H='not-accessible'
_G='none'
_F='BROCADE-SPX-MIB'
_E='DisplayString'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayString,=mibBuilder.importSymbols('FOUNDRY-SN-AGENT-MIB',_E)
snSwitch,=mibBuilder.importSymbols('FOUNDRY-SN-SWITCH-GROUP-MIB','snSwitch')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','TextualConvention')
brcdSPXMIB=ModuleIdentity((1,3,6,1,4,1,1991,1,1,3,40))
if mibBuilder.loadTexts:brcdSPXMIB.setRevisions(('2015-05-12 00:00','2017-08-07 00:00'))
_BrcdSPXGlobalObjects_ObjectIdentity=ObjectIdentity
brcdSPXGlobalObjects=_BrcdSPXGlobalObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,40,1))
class _BrcdSPXGlobalConfigCBState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_I,1),(_M,2)))
_BrcdSPXGlobalConfigCBState_Type.__name__=_C
_BrcdSPXGlobalConfigCBState_Object=MibScalar
brcdSPXGlobalConfigCBState=_BrcdSPXGlobalConfigCBState_Object((1,3,6,1,4,1,1991,1,1,3,40,1,1),_BrcdSPXGlobalConfigCBState_Type())
brcdSPXGlobalConfigCBState.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdSPXGlobalConfigCBState.setStatus(_A)
class _BrcdSPXGlobalConfigPEState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_I,1),(_M,2)))
_BrcdSPXGlobalConfigPEState_Type.__name__=_C
_BrcdSPXGlobalConfigPEState_Object=MibScalar
brcdSPXGlobalConfigPEState=_BrcdSPXGlobalConfigPEState_Object((1,3,6,1,4,1,1991,1,1,3,40,1,2),_BrcdSPXGlobalConfigPEState_Type())
brcdSPXGlobalConfigPEState.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdSPXGlobalConfigPEState.setStatus(_A)
class _BrcdSPXGlobalConfigZeroTouchEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_I,1)))
_BrcdSPXGlobalConfigZeroTouchEnable_Type.__name__=_C
_BrcdSPXGlobalConfigZeroTouchEnable_Object=MibScalar
brcdSPXGlobalConfigZeroTouchEnable=_BrcdSPXGlobalConfigZeroTouchEnable_Object((1,3,6,1,4,1,1991,1,1,3,40,1,3),_BrcdSPXGlobalConfigZeroTouchEnable_Type())
brcdSPXGlobalConfigZeroTouchEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdSPXGlobalConfigZeroTouchEnable.setStatus(_A)
class _BrcdSPXGlobalConfigZeroTouchDeny_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),('deny',1)))
_BrcdSPXGlobalConfigZeroTouchDeny_Type.__name__=_C
_BrcdSPXGlobalConfigZeroTouchDeny_Object=MibScalar
brcdSPXGlobalConfigZeroTouchDeny=_BrcdSPXGlobalConfigZeroTouchDeny_Object((1,3,6,1,4,1,1991,1,1,3,40,1,4),_BrcdSPXGlobalConfigZeroTouchDeny_Type())
brcdSPXGlobalConfigZeroTouchDeny.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdSPXGlobalConfigZeroTouchDeny.setStatus(_A)
class _BrcdSPXGlobalConfigAllowPEMovement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_I,1)))
_BrcdSPXGlobalConfigAllowPEMovement_Type.__name__=_C
_BrcdSPXGlobalConfigAllowPEMovement_Object=MibScalar
brcdSPXGlobalConfigAllowPEMovement=_BrcdSPXGlobalConfigAllowPEMovement_Object((1,3,6,1,4,1,1991,1,1,3,40,1,5),_BrcdSPXGlobalConfigAllowPEMovement_Type())
brcdSPXGlobalConfigAllowPEMovement.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdSPXGlobalConfigAllowPEMovement.setStatus(_A)
_BrcdSPXTableObjects_ObjectIdentity=ObjectIdentity
brcdSPXTableObjects=_BrcdSPXTableObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,40,2))
_BrcdSPXConfigUnitTable_Object=MibTable
brcdSPXConfigUnitTable=_BrcdSPXConfigUnitTable_Object((1,3,6,1,4,1,1991,1,1,3,40,2,1))
if mibBuilder.loadTexts:brcdSPXConfigUnitTable.setStatus(_A)
_BrcdSPXConfigUnitEntry_Object=MibTableRow
brcdSPXConfigUnitEntry=_BrcdSPXConfigUnitEntry_Object((1,3,6,1,4,1,1991,1,1,3,40,2,1,1))
brcdSPXConfigUnitEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:brcdSPXConfigUnitEntry.setStatus(_A)
_BrcdSPXConfigUnitIndex_Type=Integer32
_BrcdSPXConfigUnitIndex_Object=MibTableColumn
brcdSPXConfigUnitIndex=_BrcdSPXConfigUnitIndex_Object((1,3,6,1,4,1,1991,1,1,3,40,2,1,1,1),_BrcdSPXConfigUnitIndex_Type())
brcdSPXConfigUnitIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:brcdSPXConfigUnitIndex.setStatus(_A)
class _BrcdSPXConfigUnitPEName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrcdSPXConfigUnitPEName_Type.__name__=_E
_BrcdSPXConfigUnitPEName_Object=MibTableColumn
brcdSPXConfigUnitPEName=_BrcdSPXConfigUnitPEName_Object((1,3,6,1,4,1,1991,1,1,3,40,2,1,1,2),_BrcdSPXConfigUnitPEName_Type())
brcdSPXConfigUnitPEName.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdSPXConfigUnitPEName.setStatus(_A)
_BrcdSPXConfigUnitPESPXPort1_Type=InterfaceIndexOrZero
_BrcdSPXConfigUnitPESPXPort1_Object=MibTableColumn
brcdSPXConfigUnitPESPXPort1=_BrcdSPXConfigUnitPESPXPort1_Object((1,3,6,1,4,1,1991,1,1,3,40,2,1,1,3),_BrcdSPXConfigUnitPESPXPort1_Type())
brcdSPXConfigUnitPESPXPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdSPXConfigUnitPESPXPort1.setStatus(_A)
_BrcdSPXConfigUnitPESPXPort2_Type=InterfaceIndexOrZero
_BrcdSPXConfigUnitPESPXPort2_Object=MibTableColumn
brcdSPXConfigUnitPESPXPort2=_BrcdSPXConfigUnitPESPXPort2_Object((1,3,6,1,4,1,1991,1,1,3,40,2,1,1,4),_BrcdSPXConfigUnitPESPXPort2_Type())
brcdSPXConfigUnitPESPXPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdSPXConfigUnitPESPXPort2.setStatus(_A)
_BrcdSPXConfigUnitPESPXLag1_Type=OctetString
_BrcdSPXConfigUnitPESPXLag1_Object=MibTableColumn
brcdSPXConfigUnitPESPXLag1=_BrcdSPXConfigUnitPESPXLag1_Object((1,3,6,1,4,1,1991,1,1,3,40,2,1,1,5),_BrcdSPXConfigUnitPESPXLag1_Type())
brcdSPXConfigUnitPESPXLag1.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdSPXConfigUnitPESPXLag1.setStatus(_A)
_BrcdSPXConfigUnitPESPXLag2_Type=OctetString
_BrcdSPXConfigUnitPESPXLag2_Object=MibTableColumn
brcdSPXConfigUnitPESPXLag2=_BrcdSPXConfigUnitPESPXLag2_Object((1,3,6,1,4,1,1991,1,1,3,40,2,1,1,6),_BrcdSPXConfigUnitPESPXLag2_Type())
brcdSPXConfigUnitPESPXLag2.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdSPXConfigUnitPESPXLag2.setStatus(_A)
class _BrcdSPXConfigUnitRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3)))
_BrcdSPXConfigUnitRowStatus_Type.__name__=_C
_BrcdSPXConfigUnitRowStatus_Object=MibTableColumn
brcdSPXConfigUnitRowStatus=_BrcdSPXConfigUnitRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,40,2,1,1,7),_BrcdSPXConfigUnitRowStatus_Type())
brcdSPXConfigUnitRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdSPXConfigUnitRowStatus.setStatus(_A)
_BrcdSPXConfigUnitType_Type=DisplayString
_BrcdSPXConfigUnitType_Object=MibTableColumn
brcdSPXConfigUnitType=_BrcdSPXConfigUnitType_Object((1,3,6,1,4,1,1991,1,1,3,40,2,1,1,8),_BrcdSPXConfigUnitType_Type())
brcdSPXConfigUnitType.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdSPXConfigUnitType.setStatus(_A)
class _BrcdSPXConfigUnitState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('local',1),(_O,2),(_P,3),('empty',4)))
_BrcdSPXConfigUnitState_Type.__name__=_C
_BrcdSPXConfigUnitState_Object=MibTableColumn
brcdSPXConfigUnitState=_BrcdSPXConfigUnitState_Object((1,3,6,1,4,1,1991,1,1,3,40,2,1,1,9),_BrcdSPXConfigUnitState_Type())
brcdSPXConfigUnitState.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdSPXConfigUnitState.setStatus(_A)
_BrcdSPXOperUnitTable_Object=MibTable
brcdSPXOperUnitTable=_BrcdSPXOperUnitTable_Object((1,3,6,1,4,1,1991,1,1,3,40,2,2))
if mibBuilder.loadTexts:brcdSPXOperUnitTable.setStatus(_A)
_BrcdSPXOperUnitEntry_Object=MibTableRow
brcdSPXOperUnitEntry=_BrcdSPXOperUnitEntry_Object((1,3,6,1,4,1,1991,1,1,3,40,2,2,1))
brcdSPXOperUnitEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:brcdSPXOperUnitEntry.setStatus(_A)
_BrcdSPXOperUnitIndex_Type=Integer32
_BrcdSPXOperUnitIndex_Object=MibTableColumn
brcdSPXOperUnitIndex=_BrcdSPXOperUnitIndex_Object((1,3,6,1,4,1,1991,1,1,3,40,2,2,1,1),_BrcdSPXOperUnitIndex_Type())
brcdSPXOperUnitIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:brcdSPXOperUnitIndex.setStatus(_A)
_BrcdSPXOperUnitType_Type=DisplayString
_BrcdSPXOperUnitType_Object=MibTableColumn
brcdSPXOperUnitType=_BrcdSPXOperUnitType_Object((1,3,6,1,4,1,1991,1,1,3,40,2,2,1,2),_BrcdSPXOperUnitType_Type())
brcdSPXOperUnitType.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdSPXOperUnitType.setStatus(_A)
class _BrcdSPXOperUnitRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),('active',2),('standby',3),('member',4),('standalone',5),('spxPe',6)))
_BrcdSPXOperUnitRole_Type.__name__=_C
_BrcdSPXOperUnitRole_Object=MibTableColumn
brcdSPXOperUnitRole=_BrcdSPXOperUnitRole_Object((1,3,6,1,4,1,1991,1,1,3,40,2,2,1,3),_BrcdSPXOperUnitRole_Type())
brcdSPXOperUnitRole.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdSPXOperUnitRole.setStatus(_A)
_BrcdSPXOperUnitMac_Type=MacAddress
_BrcdSPXOperUnitMac_Object=MibTableColumn
brcdSPXOperUnitMac=_BrcdSPXOperUnitMac_Object((1,3,6,1,4,1,1991,1,1,3,40,2,2,1,4),_BrcdSPXOperUnitMac_Type())
brcdSPXOperUnitMac.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdSPXOperUnitMac.setStatus(_A)
class _BrcdSPXOperUnitPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrcdSPXOperUnitPriority_Type.__name__=_C
_BrcdSPXOperUnitPriority_Object=MibTableColumn
brcdSPXOperUnitPriority=_BrcdSPXOperUnitPriority_Object((1,3,6,1,4,1,1991,1,1,3,40,2,2,1,5),_BrcdSPXOperUnitPriority_Type())
brcdSPXOperUnitPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdSPXOperUnitPriority.setStatus(_A)
class _BrcdSPXOperUnitState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('local',1),(_O,2),(_P,3),('empty',4)))
_BrcdSPXOperUnitState_Type.__name__=_C
_BrcdSPXOperUnitState_Object=MibTableColumn
brcdSPXOperUnitState=_BrcdSPXOperUnitState_Object((1,3,6,1,4,1,1991,1,1,3,40,2,2,1,6),_BrcdSPXOperUnitState_Type())
brcdSPXOperUnitState.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdSPXOperUnitState.setStatus(_A)
class _BrcdSPXOperUnitDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_BrcdSPXOperUnitDescription_Type.__name__=_E
_BrcdSPXOperUnitDescription_Object=MibTableColumn
brcdSPXOperUnitDescription=_BrcdSPXOperUnitDescription_Object((1,3,6,1,4,1,1991,1,1,3,40,2,2,1,7),_BrcdSPXOperUnitDescription_Type())
brcdSPXOperUnitDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdSPXOperUnitDescription.setStatus(_A)
class _BrcdSPXOperUnitImgVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrcdSPXOperUnitImgVer_Type.__name__=_E
_BrcdSPXOperUnitImgVer_Object=MibTableColumn
brcdSPXOperUnitImgVer=_BrcdSPXOperUnitImgVer_Object((1,3,6,1,4,1,1991,1,1,3,40,2,2,1,8),_BrcdSPXOperUnitImgVer_Type())
brcdSPXOperUnitImgVer.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdSPXOperUnitImgVer.setStatus(_A)
class _BrcdSPXOperUnitBuildlVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrcdSPXOperUnitBuildlVer_Type.__name__=_E
_BrcdSPXOperUnitBuildlVer_Object=MibTableColumn
brcdSPXOperUnitBuildlVer=_BrcdSPXOperUnitBuildlVer_Object((1,3,6,1,4,1,1991,1,1,3,40,2,2,1,9),_BrcdSPXOperUnitBuildlVer_Type())
brcdSPXOperUnitBuildlVer.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdSPXOperUnitBuildlVer.setStatus(_A)
_BrcdSPXCBSPXPortTable_Object=MibTable
brcdSPXCBSPXPortTable=_BrcdSPXCBSPXPortTable_Object((1,3,6,1,4,1,1991,1,1,3,40,2,3))
if mibBuilder.loadTexts:brcdSPXCBSPXPortTable.setStatus(_A)
_BrcdSPXCBSPXPortEntry_Object=MibTableRow
brcdSPXCBSPXPortEntry=_BrcdSPXCBSPXPortEntry_Object((1,3,6,1,4,1,1991,1,1,3,40,2,3,1))
brcdSPXCBSPXPortEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:brcdSPXCBSPXPortEntry.setStatus(_A)
_BrcdSPXCBSPXPortPort_Type=InterfaceIndexOrZero
_BrcdSPXCBSPXPortPort_Object=MibTableColumn
brcdSPXCBSPXPortPort=_BrcdSPXCBSPXPortPort_Object((1,3,6,1,4,1,1991,1,1,3,40,2,3,1,1),_BrcdSPXCBSPXPortPort_Type())
brcdSPXCBSPXPortPort.setMaxAccess(_H)
if mibBuilder.loadTexts:brcdSPXCBSPXPortPort.setStatus(_A)
class _BrcdSPXCBSPXPortPEGroup_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrcdSPXCBSPXPortPEGroup_Type.__name__=_E
_BrcdSPXCBSPXPortPEGroup_Object=MibTableColumn
brcdSPXCBSPXPortPEGroup=_BrcdSPXCBSPXPortPEGroup_Object((1,3,6,1,4,1,1991,1,1,3,40,2,3,1,2),_BrcdSPXCBSPXPortPEGroup_Type())
brcdSPXCBSPXPortPEGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdSPXCBSPXPortPEGroup.setStatus(_A)
class _BrcdSPXCBSPXPortRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_S,4)))
_BrcdSPXCBSPXPortRowStatus_Type.__name__=_C
_BrcdSPXCBSPXPortRowStatus_Object=MibTableColumn
brcdSPXCBSPXPortRowStatus=_BrcdSPXCBSPXPortRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,40,2,3,1,3),_BrcdSPXCBSPXPortRowStatus_Type())
brcdSPXCBSPXPortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdSPXCBSPXPortRowStatus.setStatus(_A)
_BrcdSPXCBSPXLagTable_Object=MibTable
brcdSPXCBSPXLagTable=_BrcdSPXCBSPXLagTable_Object((1,3,6,1,4,1,1991,1,1,3,40,2,4))
if mibBuilder.loadTexts:brcdSPXCBSPXLagTable.setStatus(_A)
_BrcdSPXCBSPXLagEntry_Object=MibTableRow
brcdSPXCBSPXLagEntry=_BrcdSPXCBSPXLagEntry_Object((1,3,6,1,4,1,1991,1,1,3,40,2,4,1))
brcdSPXCBSPXLagEntry.setIndexNames((0,_F,_T))
if mibBuilder.loadTexts:brcdSPXCBSPXLagEntry.setStatus(_A)
_BrcdSPXCBSPXLagPrimaryPort_Type=InterfaceIndexOrZero
_BrcdSPXCBSPXLagPrimaryPort_Object=MibTableColumn
brcdSPXCBSPXLagPrimaryPort=_BrcdSPXCBSPXLagPrimaryPort_Object((1,3,6,1,4,1,1991,1,1,3,40,2,4,1,1),_BrcdSPXCBSPXLagPrimaryPort_Type())
brcdSPXCBSPXLagPrimaryPort.setMaxAccess(_H)
if mibBuilder.loadTexts:brcdSPXCBSPXLagPrimaryPort.setStatus(_A)
_BrcdSPXCBSPXLagLagIflist_Type=OctetString
_BrcdSPXCBSPXLagLagIflist_Object=MibTableColumn
brcdSPXCBSPXLagLagIflist=_BrcdSPXCBSPXLagLagIflist_Object((1,3,6,1,4,1,1991,1,1,3,40,2,4,1,2),_BrcdSPXCBSPXLagLagIflist_Type())
brcdSPXCBSPXLagLagIflist.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdSPXCBSPXLagLagIflist.setStatus(_A)
class _BrcdSPXCBSPXLagPEGroup_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrcdSPXCBSPXLagPEGroup_Type.__name__=_E
_BrcdSPXCBSPXLagPEGroup_Object=MibTableColumn
brcdSPXCBSPXLagPEGroup=_BrcdSPXCBSPXLagPEGroup_Object((1,3,6,1,4,1,1991,1,1,3,40,2,4,1,3),_BrcdSPXCBSPXLagPEGroup_Type())
brcdSPXCBSPXLagPEGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdSPXCBSPXLagPEGroup.setStatus(_A)
class _BrcdSPXCBSPXLagRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_S,4)))
_BrcdSPXCBSPXLagRowStatus_Type.__name__=_C
_BrcdSPXCBSPXLagRowStatus_Object=MibTableColumn
brcdSPXCBSPXLagRowStatus=_BrcdSPXCBSPXLagRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,40,2,4,1,4),_BrcdSPXCBSPXLagRowStatus_Type())
brcdSPXCBSPXLagRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdSPXCBSPXLagRowStatus.setStatus(_A)
_BrcdSPXPEGroupTable_Object=MibTable
brcdSPXPEGroupTable=_BrcdSPXPEGroupTable_Object((1,3,6,1,4,1,1991,1,1,3,40,2,5))
if mibBuilder.loadTexts:brcdSPXPEGroupTable.setStatus(_A)
_BrcdSPXPEGroupEntry_Object=MibTableRow
brcdSPXPEGroupEntry=_BrcdSPXPEGroupEntry_Object((1,3,6,1,4,1,1991,1,1,3,40,2,5,1))
brcdSPXPEGroupEntry.setIndexNames((0,_F,_U))
if mibBuilder.loadTexts:brcdSPXPEGroupEntry.setStatus(_A)
_BrcdSPXPEGroupCBSPXPort_Type=InterfaceIndexOrZero
_BrcdSPXPEGroupCBSPXPort_Object=MibTableColumn
brcdSPXPEGroupCBSPXPort=_BrcdSPXPEGroupCBSPXPort_Object((1,3,6,1,4,1,1991,1,1,3,40,2,5,1,1),_BrcdSPXPEGroupCBSPXPort_Type())
brcdSPXPEGroupCBSPXPort.setMaxAccess(_H)
if mibBuilder.loadTexts:brcdSPXPEGroupCBSPXPort.setStatus(_A)
_BrcdSPXPEGroupPEGroup_Type=DisplayString
_BrcdSPXPEGroupPEGroup_Object=MibTableColumn
brcdSPXPEGroupPEGroup=_BrcdSPXPEGroupPEGroup_Object((1,3,6,1,4,1,1991,1,1,3,40,2,5,1,2),_BrcdSPXPEGroupPEGroup_Type())
brcdSPXPEGroupPEGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdSPXPEGroupPEGroup.setStatus(_A)
_BrcdSPXPEGroupPEIdList_Type=DisplayString
_BrcdSPXPEGroupPEIdList_Object=MibTableColumn
brcdSPXPEGroupPEIdList=_BrcdSPXPEGroupPEIdList_Object((1,3,6,1,4,1,1991,1,1,3,40,2,5,1,3),_BrcdSPXPEGroupPEIdList_Type())
brcdSPXPEGroupPEIdList.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdSPXPEGroupPEIdList.setStatus(_A)
_BrcdSPXPEGroupCBSPXEndPort_Type=InterfaceIndexOrZero
_BrcdSPXPEGroupCBSPXEndPort_Object=MibTableColumn
brcdSPXPEGroupCBSPXEndPort=_BrcdSPXPEGroupCBSPXEndPort_Object((1,3,6,1,4,1,1991,1,1,3,40,2,5,1,4),_BrcdSPXPEGroupCBSPXEndPort_Type())
brcdSPXPEGroupCBSPXEndPort.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdSPXPEGroupCBSPXEndPort.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'brcdSPXMIB':brcdSPXMIB,'brcdSPXGlobalObjects':brcdSPXGlobalObjects,'brcdSPXGlobalConfigCBState':brcdSPXGlobalConfigCBState,'brcdSPXGlobalConfigPEState':brcdSPXGlobalConfigPEState,'brcdSPXGlobalConfigZeroTouchEnable':brcdSPXGlobalConfigZeroTouchEnable,'brcdSPXGlobalConfigZeroTouchDeny':brcdSPXGlobalConfigZeroTouchDeny,'brcdSPXGlobalConfigAllowPEMovement':brcdSPXGlobalConfigAllowPEMovement,'brcdSPXTableObjects':brcdSPXTableObjects,'brcdSPXConfigUnitTable':brcdSPXConfigUnitTable,'brcdSPXConfigUnitEntry':brcdSPXConfigUnitEntry,_N:brcdSPXConfigUnitIndex,'brcdSPXConfigUnitPEName':brcdSPXConfigUnitPEName,'brcdSPXConfigUnitPESPXPort1':brcdSPXConfigUnitPESPXPort1,'brcdSPXConfigUnitPESPXPort2':brcdSPXConfigUnitPESPXPort2,'brcdSPXConfigUnitPESPXLag1':brcdSPXConfigUnitPESPXLag1,'brcdSPXConfigUnitPESPXLag2':brcdSPXConfigUnitPESPXLag2,'brcdSPXConfigUnitRowStatus':brcdSPXConfigUnitRowStatus,'brcdSPXConfigUnitType':brcdSPXConfigUnitType,'brcdSPXConfigUnitState':brcdSPXConfigUnitState,'brcdSPXOperUnitTable':brcdSPXOperUnitTable,'brcdSPXOperUnitEntry':brcdSPXOperUnitEntry,_Q:brcdSPXOperUnitIndex,'brcdSPXOperUnitType':brcdSPXOperUnitType,'brcdSPXOperUnitRole':brcdSPXOperUnitRole,'brcdSPXOperUnitMac':brcdSPXOperUnitMac,'brcdSPXOperUnitPriority':brcdSPXOperUnitPriority,'brcdSPXOperUnitState':brcdSPXOperUnitState,'brcdSPXOperUnitDescription':brcdSPXOperUnitDescription,'brcdSPXOperUnitImgVer':brcdSPXOperUnitImgVer,'brcdSPXOperUnitBuildlVer':brcdSPXOperUnitBuildlVer,'brcdSPXCBSPXPortTable':brcdSPXCBSPXPortTable,'brcdSPXCBSPXPortEntry':brcdSPXCBSPXPortEntry,_R:brcdSPXCBSPXPortPort,'brcdSPXCBSPXPortPEGroup':brcdSPXCBSPXPortPEGroup,'brcdSPXCBSPXPortRowStatus':brcdSPXCBSPXPortRowStatus,'brcdSPXCBSPXLagTable':brcdSPXCBSPXLagTable,'brcdSPXCBSPXLagEntry':brcdSPXCBSPXLagEntry,_T:brcdSPXCBSPXLagPrimaryPort,'brcdSPXCBSPXLagLagIflist':brcdSPXCBSPXLagLagIflist,'brcdSPXCBSPXLagPEGroup':brcdSPXCBSPXLagPEGroup,'brcdSPXCBSPXLagRowStatus':brcdSPXCBSPXLagRowStatus,'brcdSPXPEGroupTable':brcdSPXPEGroupTable,'brcdSPXPEGroupEntry':brcdSPXPEGroupEntry,_U:brcdSPXPEGroupCBSPXPort,'brcdSPXPEGroupPEGroup':brcdSPXPEGroupPEGroup,'brcdSPXPEGroupPEIdList':brcdSPXPEGroupPEIdList,'brcdSPXPEGroupCBSPXEndPort':brcdSPXPEGroupCBSPXEndPort})