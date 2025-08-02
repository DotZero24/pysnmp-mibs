_P='ipadNatPortStatusLocalIpAddress'
_O='ipadNatPortStatusIndex'
_N='ipadNatPortConfigIndex'
_M='ipadNatStaticUDPTranslationEntryIndex'
_L='ipadNatStaticTCPTranslationEntryIndex'
_K='ipadNatStaticTranslationEntryIndex'
_J='DisplayString'
_I='addnew'
_H='enable'
_G='disable'
_F='IPAD-NAT-MIB'
_E='read-only'
_D='other'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ipad,=mibBuilder.importSymbols('IPADv2-MIB','ipad')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
ipadNat=ModuleIdentity((1,3,6,1,4,1,321,100,1,26))
_IpadNatParms_ObjectIdentity=ObjectIdentity
ipadNatParms=_IpadNatParms_ObjectIdentity((1,3,6,1,4,1,321,100,1,26,1))
class _IpadNatEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_IpadNatEnable_Type.__name__=_C
_IpadNatEnable_Object=MibScalar
ipadNatEnable=_IpadNatEnable_Object((1,3,6,1,4,1,321,100,1,26,1,1),_IpadNatEnable_Type())
ipadNatEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatEnable.setStatus(_A)
class _IpadNatMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('nat',2),('napt',3)))
_IpadNatMode_Type.__name__=_C
_IpadNatMode_Object=MibScalar
ipadNatMode=_IpadNatMode_Object((1,3,6,1,4,1,321,100,1,26,1,2),_IpadNatMode_Type())
ipadNatMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatMode.setStatus(_A)
_IpadNatGlobalAddress_Type=IpAddress
_IpadNatGlobalAddress_Object=MibScalar
ipadNatGlobalAddress=_IpadNatGlobalAddress_Object((1,3,6,1,4,1,321,100,1,26,1,3),_IpadNatGlobalAddress_Type())
ipadNatGlobalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatGlobalAddress.setStatus(_A)
_IpadNatGlobalMask_Type=IpAddress
_IpadNatGlobalMask_Object=MibScalar
ipadNatGlobalMask=_IpadNatGlobalMask_Object((1,3,6,1,4,1,321,100,1,26,1,4),_IpadNatGlobalMask_Type())
ipadNatGlobalMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatGlobalMask.setStatus(_A)
_IpadNatICMPDefaultAddress_Type=IpAddress
_IpadNatICMPDefaultAddress_Object=MibScalar
ipadNatICMPDefaultAddress=_IpadNatICMPDefaultAddress_Object((1,3,6,1,4,1,321,100,1,26,1,5),_IpadNatICMPDefaultAddress_Type())
ipadNatICMPDefaultAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatICMPDefaultAddress.setStatus(_A)
class _IpadNatFilterNonLocalAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_IpadNatFilterNonLocalAddress_Type.__name__=_C
_IpadNatFilterNonLocalAddress_Object=MibScalar
ipadNatFilterNonLocalAddress=_IpadNatFilterNonLocalAddress_Object((1,3,6,1,4,1,321,100,1,26,1,6),_IpadNatFilterNonLocalAddress_Type())
ipadNatFilterNonLocalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatFilterNonLocalAddress.setStatus(_A)
_IpadNatIPEntryTimer_Type=Integer32
_IpadNatIPEntryTimer_Object=MibScalar
ipadNatIPEntryTimer=_IpadNatIPEntryTimer_Object((1,3,6,1,4,1,321,100,1,26,1,7),_IpadNatIPEntryTimer_Type())
ipadNatIPEntryTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatIPEntryTimer.setStatus(_A)
_IpadNatTCPConnectionTimer_Type=Integer32
_IpadNatTCPConnectionTimer_Object=MibScalar
ipadNatTCPConnectionTimer=_IpadNatTCPConnectionTimer_Object((1,3,6,1,4,1,321,100,1,26,1,8),_IpadNatTCPConnectionTimer_Type())
ipadNatTCPConnectionTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatTCPConnectionTimer.setStatus(_A)
_IpadNatTCPClosingTimer_Type=Integer32
_IpadNatTCPClosingTimer_Object=MibScalar
ipadNatTCPClosingTimer=_IpadNatTCPClosingTimer_Object((1,3,6,1,4,1,321,100,1,26,1,9),_IpadNatTCPClosingTimer_Type())
ipadNatTCPClosingTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatTCPClosingTimer.setStatus(_A)
_IpadNatTCPDisconnectedTimer_Type=Integer32
_IpadNatTCPDisconnectedTimer_Object=MibScalar
ipadNatTCPDisconnectedTimer=_IpadNatTCPDisconnectedTimer_Object((1,3,6,1,4,1,321,100,1,26,1,10),_IpadNatTCPDisconnectedTimer_Type())
ipadNatTCPDisconnectedTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatTCPDisconnectedTimer.setStatus(_A)
_IpadNatTCPSequenceDeltaTimer_Type=Integer32
_IpadNatTCPSequenceDeltaTimer_Object=MibScalar
ipadNatTCPSequenceDeltaTimer=_IpadNatTCPSequenceDeltaTimer_Object((1,3,6,1,4,1,321,100,1,26,1,11),_IpadNatTCPSequenceDeltaTimer_Type())
ipadNatTCPSequenceDeltaTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatTCPSequenceDeltaTimer.setStatus(_A)
_IpadNatUDPTimer_Type=Integer32
_IpadNatUDPTimer_Object=MibScalar
ipadNatUDPTimer=_IpadNatUDPTimer_Object((1,3,6,1,4,1,321,100,1,26,1,12),_IpadNatUDPTimer_Type())
ipadNatUDPTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatUDPTimer.setStatus(_A)
_IpadNatICMPTimer_Type=Integer32
_IpadNatICMPTimer_Object=MibScalar
ipadNatICMPTimer=_IpadNatICMPTimer_Object((1,3,6,1,4,1,321,100,1,26,1,13),_IpadNatICMPTimer_Type())
ipadNatICMPTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatICMPTimer.setStatus(_A)
_IpadNatStaticTranslationParms_ObjectIdentity=ObjectIdentity
ipadNatStaticTranslationParms=_IpadNatStaticTranslationParms_ObjectIdentity((1,3,6,1,4,1,321,100,1,26,2))
_IpadNatStaticTranslationTable_Object=MibTable
ipadNatStaticTranslationTable=_IpadNatStaticTranslationTable_Object((1,3,6,1,4,1,321,100,1,26,2,1))
if mibBuilder.loadTexts:ipadNatStaticTranslationTable.setStatus(_A)
_IpadNatStaticTranslationTableEntry_Object=MibTableRow
ipadNatStaticTranslationTableEntry=_IpadNatStaticTranslationTableEntry_Object((1,3,6,1,4,1,321,100,1,26,2,1,1))
ipadNatStaticTranslationTableEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:ipadNatStaticTranslationTableEntry.setStatus(_A)
_IpadNatStaticTranslationEntryIndex_Type=Integer32
_IpadNatStaticTranslationEntryIndex_Object=MibTableColumn
ipadNatStaticTranslationEntryIndex=_IpadNatStaticTranslationEntryIndex_Object((1,3,6,1,4,1,321,100,1,26,2,1,1,1),_IpadNatStaticTranslationEntryIndex_Type())
ipadNatStaticTranslationEntryIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ipadNatStaticTranslationEntryIndex.setStatus(_A)
class _IpadNatStaticTranslationEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_IpadNatStaticTranslationEnable_Type.__name__=_C
_IpadNatStaticTranslationEnable_Object=MibTableColumn
ipadNatStaticTranslationEnable=_IpadNatStaticTranslationEnable_Object((1,3,6,1,4,1,321,100,1,26,2,1,1,2),_IpadNatStaticTranslationEnable_Type())
ipadNatStaticTranslationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatStaticTranslationEnable.setStatus(_A)
_IpadNatStaticTranslationLocalAddress_Type=IpAddress
_IpadNatStaticTranslationLocalAddress_Object=MibTableColumn
ipadNatStaticTranslationLocalAddress=_IpadNatStaticTranslationLocalAddress_Object((1,3,6,1,4,1,321,100,1,26,2,1,1,3),_IpadNatStaticTranslationLocalAddress_Type())
ipadNatStaticTranslationLocalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatStaticTranslationLocalAddress.setStatus(_A)
_IpadNatStaticTranslationGlobalAddress_Type=IpAddress
_IpadNatStaticTranslationGlobalAddress_Object=MibTableColumn
ipadNatStaticTranslationGlobalAddress=_IpadNatStaticTranslationGlobalAddress_Object((1,3,6,1,4,1,321,100,1,26,2,1,1,4),_IpadNatStaticTranslationGlobalAddress_Type())
ipadNatStaticTranslationGlobalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatStaticTranslationGlobalAddress.setStatus(_A)
_IpadNatStaticTCPTranslationTable_Object=MibTable
ipadNatStaticTCPTranslationTable=_IpadNatStaticTCPTranslationTable_Object((1,3,6,1,4,1,321,100,1,26,2,2))
if mibBuilder.loadTexts:ipadNatStaticTCPTranslationTable.setStatus(_A)
_IpadNatStaticTCPTranslationTableEntry_Object=MibTableRow
ipadNatStaticTCPTranslationTableEntry=_IpadNatStaticTCPTranslationTableEntry_Object((1,3,6,1,4,1,321,100,1,26,2,2,1))
ipadNatStaticTCPTranslationTableEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:ipadNatStaticTCPTranslationTableEntry.setStatus(_A)
_IpadNatStaticTCPTranslationEntryIndex_Type=Integer32
_IpadNatStaticTCPTranslationEntryIndex_Object=MibTableColumn
ipadNatStaticTCPTranslationEntryIndex=_IpadNatStaticTCPTranslationEntryIndex_Object((1,3,6,1,4,1,321,100,1,26,2,2,1,1),_IpadNatStaticTCPTranslationEntryIndex_Type())
ipadNatStaticTCPTranslationEntryIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ipadNatStaticTCPTranslationEntryIndex.setStatus(_A)
_IpadNatStaticTCPTranslationGlobalPort_Type=Integer32
_IpadNatStaticTCPTranslationGlobalPort_Object=MibTableColumn
ipadNatStaticTCPTranslationGlobalPort=_IpadNatStaticTCPTranslationGlobalPort_Object((1,3,6,1,4,1,321,100,1,26,2,2,1,2),_IpadNatStaticTCPTranslationGlobalPort_Type())
ipadNatStaticTCPTranslationGlobalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatStaticTCPTranslationGlobalPort.setStatus(_A)
_IpadNatStaticTCPTranslationServerPort_Type=Integer32
_IpadNatStaticTCPTranslationServerPort_Object=MibTableColumn
ipadNatStaticTCPTranslationServerPort=_IpadNatStaticTCPTranslationServerPort_Object((1,3,6,1,4,1,321,100,1,26,2,2,1,3),_IpadNatStaticTCPTranslationServerPort_Type())
ipadNatStaticTCPTranslationServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatStaticTCPTranslationServerPort.setStatus(_A)
_IpadNatStaticTCPTranslationServerAddress_Type=IpAddress
_IpadNatStaticTCPTranslationServerAddress_Object=MibTableColumn
ipadNatStaticTCPTranslationServerAddress=_IpadNatStaticTCPTranslationServerAddress_Object((1,3,6,1,4,1,321,100,1,26,2,2,1,4),_IpadNatStaticTCPTranslationServerAddress_Type())
ipadNatStaticTCPTranslationServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatStaticTCPTranslationServerAddress.setStatus(_A)
_IpadNatStaticUDPTranslationTable_Object=MibTable
ipadNatStaticUDPTranslationTable=_IpadNatStaticUDPTranslationTable_Object((1,3,6,1,4,1,321,100,1,26,2,3))
if mibBuilder.loadTexts:ipadNatStaticUDPTranslationTable.setStatus(_A)
_IpadNatStaticUDPTranslationTableEntry_Object=MibTableRow
ipadNatStaticUDPTranslationTableEntry=_IpadNatStaticUDPTranslationTableEntry_Object((1,3,6,1,4,1,321,100,1,26,2,3,1))
ipadNatStaticUDPTranslationTableEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:ipadNatStaticUDPTranslationTableEntry.setStatus(_A)
_IpadNatStaticUDPTranslationEntryIndex_Type=Integer32
_IpadNatStaticUDPTranslationEntryIndex_Object=MibTableColumn
ipadNatStaticUDPTranslationEntryIndex=_IpadNatStaticUDPTranslationEntryIndex_Object((1,3,6,1,4,1,321,100,1,26,2,3,1,1),_IpadNatStaticUDPTranslationEntryIndex_Type())
ipadNatStaticUDPTranslationEntryIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ipadNatStaticUDPTranslationEntryIndex.setStatus(_A)
_IpadNatStaticUDPTranslationGlobalPort_Type=Integer32
_IpadNatStaticUDPTranslationGlobalPort_Object=MibTableColumn
ipadNatStaticUDPTranslationGlobalPort=_IpadNatStaticUDPTranslationGlobalPort_Object((1,3,6,1,4,1,321,100,1,26,2,3,1,2),_IpadNatStaticUDPTranslationGlobalPort_Type())
ipadNatStaticUDPTranslationGlobalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatStaticUDPTranslationGlobalPort.setStatus(_A)
_IpadNatStaticUDPTranslationServerPort_Type=Integer32
_IpadNatStaticUDPTranslationServerPort_Object=MibTableColumn
ipadNatStaticUDPTranslationServerPort=_IpadNatStaticUDPTranslationServerPort_Object((1,3,6,1,4,1,321,100,1,26,2,3,1,3),_IpadNatStaticUDPTranslationServerPort_Type())
ipadNatStaticUDPTranslationServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatStaticUDPTranslationServerPort.setStatus(_A)
_IpadNatStaticUDPTranslationServerAddress_Type=IpAddress
_IpadNatStaticUDPTranslationServerAddress_Object=MibTableColumn
ipadNatStaticUDPTranslationServerAddress=_IpadNatStaticUDPTranslationServerAddress_Object((1,3,6,1,4,1,321,100,1,26,2,3,1,4),_IpadNatStaticUDPTranslationServerAddress_Type())
ipadNatStaticUDPTranslationServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatStaticUDPTranslationServerAddress.setStatus(_A)
class _IpadNatStaticTranslationAdd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_I,2)))
_IpadNatStaticTranslationAdd_Type.__name__=_C
_IpadNatStaticTranslationAdd_Object=MibScalar
ipadNatStaticTranslationAdd=_IpadNatStaticTranslationAdd_Object((1,3,6,1,4,1,321,100,1,26,2,4),_IpadNatStaticTranslationAdd_Type())
ipadNatStaticTranslationAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatStaticTranslationAdd.setStatus(_A)
_IpadNatStaticTranslationDelete_Type=Integer32
_IpadNatStaticTranslationDelete_Object=MibScalar
ipadNatStaticTranslationDelete=_IpadNatStaticTranslationDelete_Object((1,3,6,1,4,1,321,100,1,26,2,5),_IpadNatStaticTranslationDelete_Type())
ipadNatStaticTranslationDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatStaticTranslationDelete.setStatus(_A)
class _IpadNatStaticTCPTranslationAdd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_I,2)))
_IpadNatStaticTCPTranslationAdd_Type.__name__=_C
_IpadNatStaticTCPTranslationAdd_Object=MibScalar
ipadNatStaticTCPTranslationAdd=_IpadNatStaticTCPTranslationAdd_Object((1,3,6,1,4,1,321,100,1,26,2,6),_IpadNatStaticTCPTranslationAdd_Type())
ipadNatStaticTCPTranslationAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatStaticTCPTranslationAdd.setStatus(_A)
_IpadNatStaticTCPTranslationDelete_Type=Integer32
_IpadNatStaticTCPTranslationDelete_Object=MibScalar
ipadNatStaticTCPTranslationDelete=_IpadNatStaticTCPTranslationDelete_Object((1,3,6,1,4,1,321,100,1,26,2,7),_IpadNatStaticTCPTranslationDelete_Type())
ipadNatStaticTCPTranslationDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatStaticTCPTranslationDelete.setStatus(_A)
class _IpadNatStaticUDPTranslationAdd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_I,2)))
_IpadNatStaticUDPTranslationAdd_Type.__name__=_C
_IpadNatStaticUDPTranslationAdd_Object=MibScalar
ipadNatStaticUDPTranslationAdd=_IpadNatStaticUDPTranslationAdd_Object((1,3,6,1,4,1,321,100,1,26,2,8),_IpadNatStaticUDPTranslationAdd_Type())
ipadNatStaticUDPTranslationAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatStaticUDPTranslationAdd.setStatus(_A)
_IpadNatStaticUDPTranslationDelete_Type=Integer32
_IpadNatStaticUDPTranslationDelete_Object=MibScalar
ipadNatStaticUDPTranslationDelete=_IpadNatStaticUDPTranslationDelete_Object((1,3,6,1,4,1,321,100,1,26,2,9),_IpadNatStaticUDPTranslationDelete_Type())
ipadNatStaticUDPTranslationDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatStaticUDPTranslationDelete.setStatus(_A)
_IpadNatPortParms_ObjectIdentity=ObjectIdentity
ipadNatPortParms=_IpadNatPortParms_ObjectIdentity((1,3,6,1,4,1,321,100,1,26,3))
_IpadNatPortConfigTable_Object=MibTable
ipadNatPortConfigTable=_IpadNatPortConfigTable_Object((1,3,6,1,4,1,321,100,1,26,3,1))
if mibBuilder.loadTexts:ipadNatPortConfigTable.setStatus(_A)
_IpadNatPortConfigTableEntry_Object=MibTableRow
ipadNatPortConfigTableEntry=_IpadNatPortConfigTableEntry_Object((1,3,6,1,4,1,321,100,1,26,3,1,1))
ipadNatPortConfigTableEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:ipadNatPortConfigTableEntry.setStatus(_A)
_IpadNatPortConfigIndex_Type=Integer32
_IpadNatPortConfigIndex_Object=MibTableColumn
ipadNatPortConfigIndex=_IpadNatPortConfigIndex_Object((1,3,6,1,4,1,321,100,1,26,3,1,1,1),_IpadNatPortConfigIndex_Type())
ipadNatPortConfigIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ipadNatPortConfigIndex.setStatus(_A)
class _IpadNatPortConfigEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_IpadNatPortConfigEnable_Type.__name__=_C
_IpadNatPortConfigEnable_Object=MibTableColumn
ipadNatPortConfigEnable=_IpadNatPortConfigEnable_Object((1,3,6,1,4,1,321,100,1,26,3,1,1,2),_IpadNatPortConfigEnable_Type())
ipadNatPortConfigEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatPortConfigEnable.setStatus(_A)
class _IpadNatPortConfigDefaultTranslation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_IpadNatPortConfigDefaultTranslation_Type.__name__=_C
_IpadNatPortConfigDefaultTranslation_Object=MibTableColumn
ipadNatPortConfigDefaultTranslation=_IpadNatPortConfigDefaultTranslation_Object((1,3,6,1,4,1,321,100,1,26,3,1,1,3),_IpadNatPortConfigDefaultTranslation_Type())
ipadNatPortConfigDefaultTranslation.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatPortConfigDefaultTranslation.setStatus(_A)
class _IpadNatPortConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('global',2),('local',3)))
_IpadNatPortConfigType_Type.__name__=_C
_IpadNatPortConfigType_Object=MibTableColumn
ipadNatPortConfigType=_IpadNatPortConfigType_Object((1,3,6,1,4,1,321,100,1,26,3,1,1,4),_IpadNatPortConfigType_Type())
ipadNatPortConfigType.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatPortConfigType.setStatus(_A)
_IpadNatPortConfigIpAddress_Type=IpAddress
_IpadNatPortConfigIpAddress_Object=MibTableColumn
ipadNatPortConfigIpAddress=_IpadNatPortConfigIpAddress_Object((1,3,6,1,4,1,321,100,1,26,3,1,1,5),_IpadNatPortConfigIpAddress_Type())
ipadNatPortConfigIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatPortConfigIpAddress.setStatus(_A)
_IpadNatPortConfigMask_Type=IpAddress
_IpadNatPortConfigMask_Object=MibTableColumn
ipadNatPortConfigMask=_IpadNatPortConfigMask_Object((1,3,6,1,4,1,321,100,1,26,3,1,1,6),_IpadNatPortConfigMask_Type())
ipadNatPortConfigMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatPortConfigMask.setStatus(_A)
class _IpadNatPortConfigEndpoint_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_IpadNatPortConfigEndpoint_Type.__name__=_J
_IpadNatPortConfigEndpoint_Object=MibTableColumn
ipadNatPortConfigEndpoint=_IpadNatPortConfigEndpoint_Object((1,3,6,1,4,1,321,100,1,26,3,1,1,7),_IpadNatPortConfigEndpoint_Type())
ipadNatPortConfigEndpoint.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatPortConfigEndpoint.setStatus(_A)
class _IpadNatPortConfigClearStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),('clear',2)))
_IpadNatPortConfigClearStats_Type.__name__=_C
_IpadNatPortConfigClearStats_Object=MibTableColumn
ipadNatPortConfigClearStats=_IpadNatPortConfigClearStats_Object((1,3,6,1,4,1,321,100,1,26,3,1,1,8),_IpadNatPortConfigClearStats_Type())
ipadNatPortConfigClearStats.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatPortConfigClearStats.setStatus(_A)
class _IpadNatPortAdd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_I,2)))
_IpadNatPortAdd_Type.__name__=_C
_IpadNatPortAdd_Object=MibScalar
ipadNatPortAdd=_IpadNatPortAdd_Object((1,3,6,1,4,1,321,100,1,26,3,2),_IpadNatPortAdd_Type())
ipadNatPortAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatPortAdd.setStatus(_A)
_IpadNatPortDelete_Type=Integer32
_IpadNatPortDelete_Object=MibScalar
ipadNatPortDelete=_IpadNatPortDelete_Object((1,3,6,1,4,1,321,100,1,26,3,3),_IpadNatPortDelete_Type())
ipadNatPortDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadNatPortDelete.setStatus(_A)
_IpadNatPortStatusTable_Object=MibTable
ipadNatPortStatusTable=_IpadNatPortStatusTable_Object((1,3,6,1,4,1,321,100,1,26,3,4))
if mibBuilder.loadTexts:ipadNatPortStatusTable.setStatus(_A)
_IpadNatPortStatusTableEntry_Object=MibTableRow
ipadNatPortStatusTableEntry=_IpadNatPortStatusTableEntry_Object((1,3,6,1,4,1,321,100,1,26,3,4,1))
ipadNatPortStatusTableEntry.setIndexNames((0,_F,_O),(0,_F,_P))
if mibBuilder.loadTexts:ipadNatPortStatusTableEntry.setStatus(_A)
_IpadNatPortStatusIndex_Type=Integer32
_IpadNatPortStatusIndex_Object=MibTableColumn
ipadNatPortStatusIndex=_IpadNatPortStatusIndex_Object((1,3,6,1,4,1,321,100,1,26,3,4,1,1),_IpadNatPortStatusIndex_Type())
ipadNatPortStatusIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ipadNatPortStatusIndex.setStatus(_A)
_IpadNatPortStatusLocalIpAddress_Type=IpAddress
_IpadNatPortStatusLocalIpAddress_Object=MibTableColumn
ipadNatPortStatusLocalIpAddress=_IpadNatPortStatusLocalIpAddress_Object((1,3,6,1,4,1,321,100,1,26,3,4,1,2),_IpadNatPortStatusLocalIpAddress_Type())
ipadNatPortStatusLocalIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ipadNatPortStatusLocalIpAddress.setStatus(_A)
_IpadNatPortStatusNatIpAddress_Type=IpAddress
_IpadNatPortStatusNatIpAddress_Object=MibTableColumn
ipadNatPortStatusNatIpAddress=_IpadNatPortStatusNatIpAddress_Object((1,3,6,1,4,1,321,100,1,26,3,4,1,3),_IpadNatPortStatusNatIpAddress_Type())
ipadNatPortStatusNatIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ipadNatPortStatusNatIpAddress.setStatus(_A)
_IpadNatPortStatusTxPackets_Type=Integer32
_IpadNatPortStatusTxPackets_Object=MibTableColumn
ipadNatPortStatusTxPackets=_IpadNatPortStatusTxPackets_Object((1,3,6,1,4,1,321,100,1,26,3,4,1,4),_IpadNatPortStatusTxPackets_Type())
ipadNatPortStatusTxPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:ipadNatPortStatusTxPackets.setStatus(_A)
_IpadNatPortStatusRxPackets_Type=Integer32
_IpadNatPortStatusRxPackets_Object=MibTableColumn
ipadNatPortStatusRxPackets=_IpadNatPortStatusRxPackets_Object((1,3,6,1,4,1,321,100,1,26,3,4,1,5),_IpadNatPortStatusRxPackets_Type())
ipadNatPortStatusRxPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:ipadNatPortStatusRxPackets.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'ipadNat':ipadNat,'ipadNatParms':ipadNatParms,'ipadNatEnable':ipadNatEnable,'ipadNatMode':ipadNatMode,'ipadNatGlobalAddress':ipadNatGlobalAddress,'ipadNatGlobalMask':ipadNatGlobalMask,'ipadNatICMPDefaultAddress':ipadNatICMPDefaultAddress,'ipadNatFilterNonLocalAddress':ipadNatFilterNonLocalAddress,'ipadNatIPEntryTimer':ipadNatIPEntryTimer,'ipadNatTCPConnectionTimer':ipadNatTCPConnectionTimer,'ipadNatTCPClosingTimer':ipadNatTCPClosingTimer,'ipadNatTCPDisconnectedTimer':ipadNatTCPDisconnectedTimer,'ipadNatTCPSequenceDeltaTimer':ipadNatTCPSequenceDeltaTimer,'ipadNatUDPTimer':ipadNatUDPTimer,'ipadNatICMPTimer':ipadNatICMPTimer,'ipadNatStaticTranslationParms':ipadNatStaticTranslationParms,'ipadNatStaticTranslationTable':ipadNatStaticTranslationTable,'ipadNatStaticTranslationTableEntry':ipadNatStaticTranslationTableEntry,_K:ipadNatStaticTranslationEntryIndex,'ipadNatStaticTranslationEnable':ipadNatStaticTranslationEnable,'ipadNatStaticTranslationLocalAddress':ipadNatStaticTranslationLocalAddress,'ipadNatStaticTranslationGlobalAddress':ipadNatStaticTranslationGlobalAddress,'ipadNatStaticTCPTranslationTable':ipadNatStaticTCPTranslationTable,'ipadNatStaticTCPTranslationTableEntry':ipadNatStaticTCPTranslationTableEntry,_L:ipadNatStaticTCPTranslationEntryIndex,'ipadNatStaticTCPTranslationGlobalPort':ipadNatStaticTCPTranslationGlobalPort,'ipadNatStaticTCPTranslationServerPort':ipadNatStaticTCPTranslationServerPort,'ipadNatStaticTCPTranslationServerAddress':ipadNatStaticTCPTranslationServerAddress,'ipadNatStaticUDPTranslationTable':ipadNatStaticUDPTranslationTable,'ipadNatStaticUDPTranslationTableEntry':ipadNatStaticUDPTranslationTableEntry,_M:ipadNatStaticUDPTranslationEntryIndex,'ipadNatStaticUDPTranslationGlobalPort':ipadNatStaticUDPTranslationGlobalPort,'ipadNatStaticUDPTranslationServerPort':ipadNatStaticUDPTranslationServerPort,'ipadNatStaticUDPTranslationServerAddress':ipadNatStaticUDPTranslationServerAddress,'ipadNatStaticTranslationAdd':ipadNatStaticTranslationAdd,'ipadNatStaticTranslationDelete':ipadNatStaticTranslationDelete,'ipadNatStaticTCPTranslationAdd':ipadNatStaticTCPTranslationAdd,'ipadNatStaticTCPTranslationDelete':ipadNatStaticTCPTranslationDelete,'ipadNatStaticUDPTranslationAdd':ipadNatStaticUDPTranslationAdd,'ipadNatStaticUDPTranslationDelete':ipadNatStaticUDPTranslationDelete,'ipadNatPortParms':ipadNatPortParms,'ipadNatPortConfigTable':ipadNatPortConfigTable,'ipadNatPortConfigTableEntry':ipadNatPortConfigTableEntry,_N:ipadNatPortConfigIndex,'ipadNatPortConfigEnable':ipadNatPortConfigEnable,'ipadNatPortConfigDefaultTranslation':ipadNatPortConfigDefaultTranslation,'ipadNatPortConfigType':ipadNatPortConfigType,'ipadNatPortConfigIpAddress':ipadNatPortConfigIpAddress,'ipadNatPortConfigMask':ipadNatPortConfigMask,'ipadNatPortConfigEndpoint':ipadNatPortConfigEndpoint,'ipadNatPortConfigClearStats':ipadNatPortConfigClearStats,'ipadNatPortAdd':ipadNatPortAdd,'ipadNatPortDelete':ipadNatPortDelete,'ipadNatPortStatusTable':ipadNatPortStatusTable,'ipadNatPortStatusTableEntry':ipadNatPortStatusTableEntry,_O:ipadNatPortStatusIndex,_P:ipadNatPortStatusLocalIpAddress,'ipadNatPortStatusNatIpAddress':ipadNatPortStatusNatIpAddress,'ipadNatPortStatusTxPackets':ipadNatPortStatusTxPackets,'ipadNatPortStatusRxPackets':ipadNatPortStatusRxPackets})