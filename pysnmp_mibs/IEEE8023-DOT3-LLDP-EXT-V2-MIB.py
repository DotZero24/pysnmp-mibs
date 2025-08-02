_AQ='lldpV2Xdot3RemSysGroup'
_AP='lldpV2Xdot3LocSysGroup'
_AO='lldpV2Xdot3ConfigGroup'
_AN='lldpV2Xdot3RemFbTwSys'
_AM='lldpV2Xdot3RemRxTwSysEcho'
_AL='lldpV2Xdot3RemRxTwSys'
_AK='lldpV2Xdot3RemTxTwSysEcho'
_AJ='lldpV2Xdot3RemTxTwSys'
_AI='lldpV2Xdot3RemPSEAllocatedPowerValue'
_AH='lldpV2Xdot3RemPDRequestedPowerValue'
_AG='lldpV2Xdot3RemPowerPriority'
_AF='lldpV2Xdot3RemPowerSource'
_AE='lldpV2Xdot3RemPowerType'
_AD='lldpV2Xdot3RemMaxFrameSize'
_AC='lldpV2Xdot3RemPowerClass'
_AB='lldpV2Xdot3RemPowerPairs'
_AA='lldpV2Xdot3RemPowerPairControlable'
_A9='lldpV2Xdot3RemPowerMDIEnabled'
_A8='lldpV2Xdot3RemPowerMDISupported'
_A7='lldpV2Xdot3RemPowerPortClass'
_A6='lldpV2Xdot3RemPortOperMauType'
_A5='lldpV2Xdot3RemPortAutoNegAdvertisedCap'
_A4='lldpV2Xdot3RemPortAutoNegEnabled'
_A3='lldpV2Xdot3RemPortAutoNegSupported'
_A2='lldpV2Xdot3LocDllEnabled'
_A1='lldpV2Xdot3RxDllReady'
_A0='lldpV2Xdot3TxDllReady'
_z='lldpV2Xdot3LocFbTwSys'
_y='lldpV2Xdot3LocRxTwSysEcho'
_x='lldpV2Xdot3LocRxTwSys'
_w='lldpV2Xdot3LocTxTwSysEcho'
_v='lldpV2Xdot3LocTxTwSys'
_u='lldpV2Xdot3LocReducedOperationPowerValue'
_t='lldpV2Xdot3LocReady'
_s='lldpV2Xdot3LocResponseTime'
_r='lldpV2Xdot3LocPSEAllocatedPowerValue'
_q='lldpV2Xdot3LocPDRequestedPowerValue'
_p='lldpV2Xdot3LocPowerPriority'
_o='lldpV2Xdot3LocPowerSource'
_n='lldpV2Xdot3LocPowerType'
_m='lldpV2Xdot3LocMaxFrameSize'
_l='lldpV2Xdot3LocPowerClass'
_k='lldpV2Xdot3LocPowerPairs'
_j='lldpV2Xdot3LocPowerPairControlable'
_i='lldpV2Xdot3LocPowerMDIEnabled'
_h='lldpV2Xdot3LocPowerMDISupported'
_g='lldpV2Xdot3LocPowerPortClass'
_f='lldpV2Xdot3LocPortOperMauType'
_e='lldpV2Xdot3LocPortAutoNegAdvertisedCap'
_d='lldpV2Xdot3LocPortAutoNegEnabled'
_c='lldpV2Xdot3LocPortAutoNegSupported'
_b='lldpV2Xdot3PortConfigTLVsTxEnable'
_a='lldpV2Xdot3PortConfigEntry'
_Z='unknown'
_Y='critical'
_X='pdunknown'
_W='pdpseonly'
_V='pdpseandlocal'
_U='pseunknown'
_T='psebackup'
_S='pseprimary'
_R='pdtype2'
_Q='pdtype'
_P='psetype2'
_O='psetype1'
_N='ifGeneralInformationGroup'
_M='read-write'
_L='OctetString'
_K='lldpV2RemTimeMark'
_J='lldpV2RemLocalDestMACAddress'
_I='lldpV2RemIndex'
_H='lldpV2RemLocalIfIndex'
_G='lldpV2LocPortIfIndex'
_F='Integer32'
_E='Unsigned32'
_D='LLDP-V2-MIB'
_C='read-only'
_B='IEEE8023-DOT3-LLDP-EXT-V2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifGeneralInformationGroup,=mibBuilder.importSymbols('IF-MIB',_N)
lldpV2LocPortIfIndex,lldpV2PortConfigEntry,lldpV2RemIndex,lldpV2RemLocalDestMACAddress,lldpV2RemLocalIfIndex,lldpV2RemTimeMark=mibBuilder.importSymbols(_D,_G,'lldpV2PortConfigEntry',_I,_J,_H,_K)
LldpV2PowerPortClass,=mibBuilder.importSymbols('LLDP-V2-TC-MIB','LldpV2PowerPortClass')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,org=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso','org')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ieee8023lldpV2Xdot3MIB=ModuleIdentity((1,3,111,2,802,3,1,5))
if mibBuilder.loadTexts:ieee8023lldpV2Xdot3MIB.setRevisions(('2013-04-11 00:00','2011-02-02 00:00'))
_LldpV2Xdot3Objects_ObjectIdentity=ObjectIdentity
lldpV2Xdot3Objects=_LldpV2Xdot3Objects_ObjectIdentity((1,3,111,2,802,3,1,5,1))
_LldpV2Xdot3Config_ObjectIdentity=ObjectIdentity
lldpV2Xdot3Config=_LldpV2Xdot3Config_ObjectIdentity((1,3,111,2,802,3,1,5,1,1))
_LldpV2Xdot3PortConfigTable_Object=MibTable
lldpV2Xdot3PortConfigTable=_LldpV2Xdot3PortConfigTable_Object((1,3,111,2,802,3,1,5,1,1,1))
if mibBuilder.loadTexts:lldpV2Xdot3PortConfigTable.setStatus(_A)
_LldpV2Xdot3PortConfigEntry_Object=MibTableRow
lldpV2Xdot3PortConfigEntry=_LldpV2Xdot3PortConfigEntry_Object((1,3,111,2,802,3,1,5,1,1,1,1))
if mibBuilder.loadTexts:lldpV2Xdot3PortConfigEntry.setStatus(_A)
class _LldpV2Xdot3PortConfigTLVsTxEnable_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('macPhyConfigStatus',0),('powerViaMDI',1),('unused',2),('maxFrameSize',3)))
_LldpV2Xdot3PortConfigTLVsTxEnable_Type.__name__='Bits'
_LldpV2Xdot3PortConfigTLVsTxEnable_Object=MibTableColumn
lldpV2Xdot3PortConfigTLVsTxEnable=_LldpV2Xdot3PortConfigTLVsTxEnable_Object((1,3,111,2,802,3,1,5,1,1,1,1,1),_LldpV2Xdot3PortConfigTLVsTxEnable_Type())
lldpV2Xdot3PortConfigTLVsTxEnable.setMaxAccess(_M)
if mibBuilder.loadTexts:lldpV2Xdot3PortConfigTLVsTxEnable.setStatus(_A)
_LldpV2Xdot3LocalData_ObjectIdentity=ObjectIdentity
lldpV2Xdot3LocalData=_LldpV2Xdot3LocalData_ObjectIdentity((1,3,111,2,802,3,1,5,1,2))
_LldpV2Xdot3LocPortTable_Object=MibTable
lldpV2Xdot3LocPortTable=_LldpV2Xdot3LocPortTable_Object((1,3,111,2,802,3,1,5,1,2,1))
if mibBuilder.loadTexts:lldpV2Xdot3LocPortTable.setStatus(_A)
_LldpV2Xdot3LocPortEntry_Object=MibTableRow
lldpV2Xdot3LocPortEntry=_LldpV2Xdot3LocPortEntry_Object((1,3,111,2,802,3,1,5,1,2,1,1))
lldpV2Xdot3LocPortEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:lldpV2Xdot3LocPortEntry.setStatus(_A)
_LldpV2Xdot3LocPortAutoNegSupported_Type=TruthValue
_LldpV2Xdot3LocPortAutoNegSupported_Object=MibTableColumn
lldpV2Xdot3LocPortAutoNegSupported=_LldpV2Xdot3LocPortAutoNegSupported_Object((1,3,111,2,802,3,1,5,1,2,1,1,1),_LldpV2Xdot3LocPortAutoNegSupported_Type())
lldpV2Xdot3LocPortAutoNegSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPortAutoNegSupported.setStatus(_A)
_LldpV2Xdot3LocPortAutoNegEnabled_Type=TruthValue
_LldpV2Xdot3LocPortAutoNegEnabled_Object=MibTableColumn
lldpV2Xdot3LocPortAutoNegEnabled=_LldpV2Xdot3LocPortAutoNegEnabled_Object((1,3,111,2,802,3,1,5,1,2,1,1,2),_LldpV2Xdot3LocPortAutoNegEnabled_Type())
lldpV2Xdot3LocPortAutoNegEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPortAutoNegEnabled.setStatus(_A)
class _LldpV2Xdot3LocPortAutoNegAdvertisedCap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_LldpV2Xdot3LocPortAutoNegAdvertisedCap_Type.__name__=_L
_LldpV2Xdot3LocPortAutoNegAdvertisedCap_Object=MibTableColumn
lldpV2Xdot3LocPortAutoNegAdvertisedCap=_LldpV2Xdot3LocPortAutoNegAdvertisedCap_Object((1,3,111,2,802,3,1,5,1,2,1,1,3),_LldpV2Xdot3LocPortAutoNegAdvertisedCap_Type())
lldpV2Xdot3LocPortAutoNegAdvertisedCap.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPortAutoNegAdvertisedCap.setStatus(_A)
class _LldpV2Xdot3LocPortOperMauType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_LldpV2Xdot3LocPortOperMauType_Type.__name__=_E
_LldpV2Xdot3LocPortOperMauType_Object=MibTableColumn
lldpV2Xdot3LocPortOperMauType=_LldpV2Xdot3LocPortOperMauType_Object((1,3,111,2,802,3,1,5,1,2,1,1,4),_LldpV2Xdot3LocPortOperMauType_Type())
lldpV2Xdot3LocPortOperMauType.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPortOperMauType.setStatus(_A)
_LldpV2Xdot3LocPowerTable_Object=MibTable
lldpV2Xdot3LocPowerTable=_LldpV2Xdot3LocPowerTable_Object((1,3,111,2,802,3,1,5,1,2,2))
if mibBuilder.loadTexts:lldpV2Xdot3LocPowerTable.setStatus(_A)
_LldpV2Xdot3LocPowerEntry_Object=MibTableRow
lldpV2Xdot3LocPowerEntry=_LldpV2Xdot3LocPowerEntry_Object((1,3,111,2,802,3,1,5,1,2,2,1))
lldpV2Xdot3LocPowerEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:lldpV2Xdot3LocPowerEntry.setStatus(_A)
_LldpV2Xdot3LocPowerPortClass_Type=LldpV2PowerPortClass
_LldpV2Xdot3LocPowerPortClass_Object=MibTableColumn
lldpV2Xdot3LocPowerPortClass=_LldpV2Xdot3LocPowerPortClass_Object((1,3,111,2,802,3,1,5,1,2,2,1,1),_LldpV2Xdot3LocPowerPortClass_Type())
lldpV2Xdot3LocPowerPortClass.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPowerPortClass.setStatus(_A)
_LldpV2Xdot3LocPowerMDISupported_Type=TruthValue
_LldpV2Xdot3LocPowerMDISupported_Object=MibTableColumn
lldpV2Xdot3LocPowerMDISupported=_LldpV2Xdot3LocPowerMDISupported_Object((1,3,111,2,802,3,1,5,1,2,2,1,2),_LldpV2Xdot3LocPowerMDISupported_Type())
lldpV2Xdot3LocPowerMDISupported.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPowerMDISupported.setStatus(_A)
_LldpV2Xdot3LocPowerMDIEnabled_Type=TruthValue
_LldpV2Xdot3LocPowerMDIEnabled_Object=MibTableColumn
lldpV2Xdot3LocPowerMDIEnabled=_LldpV2Xdot3LocPowerMDIEnabled_Object((1,3,111,2,802,3,1,5,1,2,2,1,3),_LldpV2Xdot3LocPowerMDIEnabled_Type())
lldpV2Xdot3LocPowerMDIEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPowerMDIEnabled.setStatus(_A)
_LldpV2Xdot3LocPowerPairControlable_Type=TruthValue
_LldpV2Xdot3LocPowerPairControlable_Object=MibTableColumn
lldpV2Xdot3LocPowerPairControlable=_LldpV2Xdot3LocPowerPairControlable_Object((1,3,111,2,802,3,1,5,1,2,2,1,4),_LldpV2Xdot3LocPowerPairControlable_Type())
lldpV2Xdot3LocPowerPairControlable.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPowerPairControlable.setStatus(_A)
class _LldpV2Xdot3LocPowerPairs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_LldpV2Xdot3LocPowerPairs_Type.__name__=_E
_LldpV2Xdot3LocPowerPairs_Object=MibTableColumn
lldpV2Xdot3LocPowerPairs=_LldpV2Xdot3LocPowerPairs_Object((1,3,111,2,802,3,1,5,1,2,2,1,5),_LldpV2Xdot3LocPowerPairs_Type())
lldpV2Xdot3LocPowerPairs.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPowerPairs.setStatus(_A)
class _LldpV2Xdot3LocPowerClass_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2),ValueRangeConstraint(3,3),ValueRangeConstraint(4,4),ValueRangeConstraint(5,5))
_LldpV2Xdot3LocPowerClass_Type.__name__=_E
_LldpV2Xdot3LocPowerClass_Object=MibTableColumn
lldpV2Xdot3LocPowerClass=_LldpV2Xdot3LocPowerClass_Object((1,3,111,2,802,3,1,5,1,2,2,1,6),_LldpV2Xdot3LocPowerClass_Type())
lldpV2Xdot3LocPowerClass.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPowerClass.setStatus(_A)
class _LldpV2Xdot3LocPowerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_O,0),(_P,1),(_Q,2),(_R,3)))
_LldpV2Xdot3LocPowerType_Type.__name__=_F
_LldpV2Xdot3LocPowerType_Object=MibTableColumn
lldpV2Xdot3LocPowerType=_LldpV2Xdot3LocPowerType_Object((1,3,111,2,802,3,1,5,1,2,2,1,7),_LldpV2Xdot3LocPowerType_Type())
lldpV2Xdot3LocPowerType.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPowerType.setStatus(_A)
class _LldpV2Xdot3LocPowerSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_S,0),(_T,1),(_U,2),(_V,3),(_W,4),(_X,5)))
_LldpV2Xdot3LocPowerSource_Type.__name__=_F
_LldpV2Xdot3LocPowerSource_Object=MibTableColumn
lldpV2Xdot3LocPowerSource=_LldpV2Xdot3LocPowerSource_Object((1,3,111,2,802,3,1,5,1,2,2,1,8),_LldpV2Xdot3LocPowerSource_Type())
lldpV2Xdot3LocPowerSource.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPowerSource.setStatus(_A)
class _LldpV2Xdot3LocPowerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('low',0),('high',1),(_Y,2),(_Z,3)))
_LldpV2Xdot3LocPowerPriority_Type.__name__=_F
_LldpV2Xdot3LocPowerPriority_Object=MibTableColumn
lldpV2Xdot3LocPowerPriority=_LldpV2Xdot3LocPowerPriority_Object((1,3,111,2,802,3,1,5,1,2,2,1,9),_LldpV2Xdot3LocPowerPriority_Type())
lldpV2Xdot3LocPowerPriority.setMaxAccess(_M)
if mibBuilder.loadTexts:lldpV2Xdot3LocPowerPriority.setStatus(_A)
_LldpV2Xdot3LocPDRequestedPowerValue_Type=Integer32
_LldpV2Xdot3LocPDRequestedPowerValue_Object=MibTableColumn
lldpV2Xdot3LocPDRequestedPowerValue=_LldpV2Xdot3LocPDRequestedPowerValue_Object((1,3,111,2,802,3,1,5,1,2,2,1,10),_LldpV2Xdot3LocPDRequestedPowerValue_Type())
lldpV2Xdot3LocPDRequestedPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPDRequestedPowerValue.setStatus(_A)
_LldpV2Xdot3LocPSEAllocatedPowerValue_Type=Integer32
_LldpV2Xdot3LocPSEAllocatedPowerValue_Object=MibTableColumn
lldpV2Xdot3LocPSEAllocatedPowerValue=_LldpV2Xdot3LocPSEAllocatedPowerValue_Object((1,3,111,2,802,3,1,5,1,2,2,1,11),_LldpV2Xdot3LocPSEAllocatedPowerValue_Type())
lldpV2Xdot3LocPSEAllocatedPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPSEAllocatedPowerValue.setStatus(_A)
_LldpV2Xdot3LocResponseTime_Type=Integer32
_LldpV2Xdot3LocResponseTime_Object=MibTableColumn
lldpV2Xdot3LocResponseTime=_LldpV2Xdot3LocResponseTime_Object((1,3,111,2,802,3,1,5,1,2,2,1,12),_LldpV2Xdot3LocResponseTime_Type())
lldpV2Xdot3LocResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocResponseTime.setStatus(_A)
_LldpV2Xdot3LocReady_Type=TruthValue
_LldpV2Xdot3LocReady_Object=MibTableColumn
lldpV2Xdot3LocReady=_LldpV2Xdot3LocReady_Object((1,3,111,2,802,3,1,5,1,2,2,1,13),_LldpV2Xdot3LocReady_Type())
lldpV2Xdot3LocReady.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocReady.setStatus(_A)
_LldpV2Xdot3LocReducedOperationPowerValue_Type=Integer32
_LldpV2Xdot3LocReducedOperationPowerValue_Object=MibTableColumn
lldpV2Xdot3LocReducedOperationPowerValue=_LldpV2Xdot3LocReducedOperationPowerValue_Object((1,3,111,2,802,3,1,5,1,2,2,1,14),_LldpV2Xdot3LocReducedOperationPowerValue_Type())
lldpV2Xdot3LocReducedOperationPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocReducedOperationPowerValue.setStatus(_A)
_LldpV2Xdot3LocMaxFrameSizeTable_Object=MibTable
lldpV2Xdot3LocMaxFrameSizeTable=_LldpV2Xdot3LocMaxFrameSizeTable_Object((1,3,111,2,802,3,1,5,1,2,3))
if mibBuilder.loadTexts:lldpV2Xdot3LocMaxFrameSizeTable.setStatus(_A)
_LldpV2Xdot3LocMaxFrameSizeEntry_Object=MibTableRow
lldpV2Xdot3LocMaxFrameSizeEntry=_LldpV2Xdot3LocMaxFrameSizeEntry_Object((1,3,111,2,802,3,1,5,1,2,3,1))
lldpV2Xdot3LocMaxFrameSizeEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:lldpV2Xdot3LocMaxFrameSizeEntry.setStatus(_A)
class _LldpV2Xdot3LocMaxFrameSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LldpV2Xdot3LocMaxFrameSize_Type.__name__=_E
_LldpV2Xdot3LocMaxFrameSize_Object=MibTableColumn
lldpV2Xdot3LocMaxFrameSize=_LldpV2Xdot3LocMaxFrameSize_Object((1,3,111,2,802,3,1,5,1,2,3,1,1),_LldpV2Xdot3LocMaxFrameSize_Type())
lldpV2Xdot3LocMaxFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocMaxFrameSize.setStatus(_A)
_LldpV2Xdot3LocEEETable_Object=MibTable
lldpV2Xdot3LocEEETable=_LldpV2Xdot3LocEEETable_Object((1,3,111,2,802,3,1,5,1,2,4))
if mibBuilder.loadTexts:lldpV2Xdot3LocEEETable.setStatus(_A)
_LldpV2Xdot3LocEEEEntry_Object=MibTableRow
lldpV2Xdot3LocEEEEntry=_LldpV2Xdot3LocEEEEntry_Object((1,3,111,2,802,3,1,5,1,2,4,1))
lldpV2Xdot3LocEEEEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:lldpV2Xdot3LocEEEEntry.setStatus(_A)
_LldpV2Xdot3LocTxTwSys_Type=Integer32
_LldpV2Xdot3LocTxTwSys_Object=MibTableColumn
lldpV2Xdot3LocTxTwSys=_LldpV2Xdot3LocTxTwSys_Object((1,3,111,2,802,3,1,5,1,2,4,1,1),_LldpV2Xdot3LocTxTwSys_Type())
lldpV2Xdot3LocTxTwSys.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocTxTwSys.setStatus(_A)
_LldpV2Xdot3LocTxTwSysEcho_Type=Integer32
_LldpV2Xdot3LocTxTwSysEcho_Object=MibTableColumn
lldpV2Xdot3LocTxTwSysEcho=_LldpV2Xdot3LocTxTwSysEcho_Object((1,3,111,2,802,3,1,5,1,2,4,1,2),_LldpV2Xdot3LocTxTwSysEcho_Type())
lldpV2Xdot3LocTxTwSysEcho.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocTxTwSysEcho.setStatus(_A)
_LldpV2Xdot3LocRxTwSys_Type=Integer32
_LldpV2Xdot3LocRxTwSys_Object=MibTableColumn
lldpV2Xdot3LocRxTwSys=_LldpV2Xdot3LocRxTwSys_Object((1,3,111,2,802,3,1,5,1,2,4,1,3),_LldpV2Xdot3LocRxTwSys_Type())
lldpV2Xdot3LocRxTwSys.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocRxTwSys.setStatus(_A)
_LldpV2Xdot3LocRxTwSysEcho_Type=Integer32
_LldpV2Xdot3LocRxTwSysEcho_Object=MibTableColumn
lldpV2Xdot3LocRxTwSysEcho=_LldpV2Xdot3LocRxTwSysEcho_Object((1,3,111,2,802,3,1,5,1,2,4,1,4),_LldpV2Xdot3LocRxTwSysEcho_Type())
lldpV2Xdot3LocRxTwSysEcho.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocRxTwSysEcho.setStatus(_A)
_LldpV2Xdot3LocFbTwSys_Type=Integer32
_LldpV2Xdot3LocFbTwSys_Object=MibTableColumn
lldpV2Xdot3LocFbTwSys=_LldpV2Xdot3LocFbTwSys_Object((1,3,111,2,802,3,1,5,1,2,4,1,5),_LldpV2Xdot3LocFbTwSys_Type())
lldpV2Xdot3LocFbTwSys.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocFbTwSys.setStatus(_A)
_LldpV2Xdot3TxDllReady_Type=TruthValue
_LldpV2Xdot3TxDllReady_Object=MibTableColumn
lldpV2Xdot3TxDllReady=_LldpV2Xdot3TxDllReady_Object((1,3,111,2,802,3,1,5,1,2,4,1,6),_LldpV2Xdot3TxDllReady_Type())
lldpV2Xdot3TxDllReady.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3TxDllReady.setStatus(_A)
_LldpV2Xdot3RxDllReady_Type=TruthValue
_LldpV2Xdot3RxDllReady_Object=MibTableColumn
lldpV2Xdot3RxDllReady=_LldpV2Xdot3RxDllReady_Object((1,3,111,2,802,3,1,5,1,2,4,1,7),_LldpV2Xdot3RxDllReady_Type())
lldpV2Xdot3RxDllReady.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RxDllReady.setStatus(_A)
_LldpV2Xdot3LocDllEnabled_Type=TruthValue
_LldpV2Xdot3LocDllEnabled_Object=MibTableColumn
lldpV2Xdot3LocDllEnabled=_LldpV2Xdot3LocDllEnabled_Object((1,3,111,2,802,3,1,5,1,2,4,1,8),_LldpV2Xdot3LocDllEnabled_Type())
lldpV2Xdot3LocDllEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocDllEnabled.setStatus(_A)
_LldpV2Xdot3RemoteData_ObjectIdentity=ObjectIdentity
lldpV2Xdot3RemoteData=_LldpV2Xdot3RemoteData_ObjectIdentity((1,3,111,2,802,3,1,5,1,3))
_LldpV2Xdot3RemPortTable_Object=MibTable
lldpV2Xdot3RemPortTable=_LldpV2Xdot3RemPortTable_Object((1,3,111,2,802,3,1,5,1,3,1))
if mibBuilder.loadTexts:lldpV2Xdot3RemPortTable.setStatus(_A)
_LldpV2Xdot3RemPortEntry_Object=MibTableRow
lldpV2Xdot3RemPortEntry=_LldpV2Xdot3RemPortEntry_Object((1,3,111,2,802,3,1,5,1,3,1,1))
lldpV2Xdot3RemPortEntry.setIndexNames((0,_D,_K),(0,_D,_H),(0,_D,_J),(0,_D,_I))
if mibBuilder.loadTexts:lldpV2Xdot3RemPortEntry.setStatus(_A)
_LldpV2Xdot3RemPortAutoNegSupported_Type=TruthValue
_LldpV2Xdot3RemPortAutoNegSupported_Object=MibTableColumn
lldpV2Xdot3RemPortAutoNegSupported=_LldpV2Xdot3RemPortAutoNegSupported_Object((1,3,111,2,802,3,1,5,1,3,1,1,1),_LldpV2Xdot3RemPortAutoNegSupported_Type())
lldpV2Xdot3RemPortAutoNegSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPortAutoNegSupported.setStatus(_A)
_LldpV2Xdot3RemPortAutoNegEnabled_Type=TruthValue
_LldpV2Xdot3RemPortAutoNegEnabled_Object=MibTableColumn
lldpV2Xdot3RemPortAutoNegEnabled=_LldpV2Xdot3RemPortAutoNegEnabled_Object((1,3,111,2,802,3,1,5,1,3,1,1,2),_LldpV2Xdot3RemPortAutoNegEnabled_Type())
lldpV2Xdot3RemPortAutoNegEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPortAutoNegEnabled.setStatus(_A)
class _LldpV2Xdot3RemPortAutoNegAdvertisedCap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_LldpV2Xdot3RemPortAutoNegAdvertisedCap_Type.__name__=_L
_LldpV2Xdot3RemPortAutoNegAdvertisedCap_Object=MibTableColumn
lldpV2Xdot3RemPortAutoNegAdvertisedCap=_LldpV2Xdot3RemPortAutoNegAdvertisedCap_Object((1,3,111,2,802,3,1,5,1,3,1,1,3),_LldpV2Xdot3RemPortAutoNegAdvertisedCap_Type())
lldpV2Xdot3RemPortAutoNegAdvertisedCap.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPortAutoNegAdvertisedCap.setStatus(_A)
class _LldpV2Xdot3RemPortOperMauType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_LldpV2Xdot3RemPortOperMauType_Type.__name__=_E
_LldpV2Xdot3RemPortOperMauType_Object=MibTableColumn
lldpV2Xdot3RemPortOperMauType=_LldpV2Xdot3RemPortOperMauType_Object((1,3,111,2,802,3,1,5,1,3,1,1,4),_LldpV2Xdot3RemPortOperMauType_Type())
lldpV2Xdot3RemPortOperMauType.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPortOperMauType.setStatus(_A)
_LldpV2Xdot3RemPowerTable_Object=MibTable
lldpV2Xdot3RemPowerTable=_LldpV2Xdot3RemPowerTable_Object((1,3,111,2,802,3,1,5,1,3,2))
if mibBuilder.loadTexts:lldpV2Xdot3RemPowerTable.setStatus(_A)
_LldpV2Xdot3RemPowerEntry_Object=MibTableRow
lldpV2Xdot3RemPowerEntry=_LldpV2Xdot3RemPowerEntry_Object((1,3,111,2,802,3,1,5,1,3,2,1))
lldpV2Xdot3RemPowerEntry.setIndexNames((0,_D,_K),(0,_D,_H),(0,_D,_J),(0,_D,_I))
if mibBuilder.loadTexts:lldpV2Xdot3RemPowerEntry.setStatus(_A)
_LldpV2Xdot3RemPowerPortClass_Type=LldpV2PowerPortClass
_LldpV2Xdot3RemPowerPortClass_Object=MibTableColumn
lldpV2Xdot3RemPowerPortClass=_LldpV2Xdot3RemPowerPortClass_Object((1,3,111,2,802,3,1,5,1,3,2,1,1),_LldpV2Xdot3RemPowerPortClass_Type())
lldpV2Xdot3RemPowerPortClass.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPowerPortClass.setStatus(_A)
_LldpV2Xdot3RemPowerMDISupported_Type=TruthValue
_LldpV2Xdot3RemPowerMDISupported_Object=MibTableColumn
lldpV2Xdot3RemPowerMDISupported=_LldpV2Xdot3RemPowerMDISupported_Object((1,3,111,2,802,3,1,5,1,3,2,1,2),_LldpV2Xdot3RemPowerMDISupported_Type())
lldpV2Xdot3RemPowerMDISupported.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPowerMDISupported.setStatus(_A)
_LldpV2Xdot3RemPowerMDIEnabled_Type=TruthValue
_LldpV2Xdot3RemPowerMDIEnabled_Object=MibTableColumn
lldpV2Xdot3RemPowerMDIEnabled=_LldpV2Xdot3RemPowerMDIEnabled_Object((1,3,111,2,802,3,1,5,1,3,2,1,3),_LldpV2Xdot3RemPowerMDIEnabled_Type())
lldpV2Xdot3RemPowerMDIEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPowerMDIEnabled.setStatus(_A)
_LldpV2Xdot3RemPowerPairControlable_Type=TruthValue
_LldpV2Xdot3RemPowerPairControlable_Object=MibTableColumn
lldpV2Xdot3RemPowerPairControlable=_LldpV2Xdot3RemPowerPairControlable_Object((1,3,111,2,802,3,1,5,1,3,2,1,4),_LldpV2Xdot3RemPowerPairControlable_Type())
lldpV2Xdot3RemPowerPairControlable.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPowerPairControlable.setStatus(_A)
class _LldpV2Xdot3RemPowerPairs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_LldpV2Xdot3RemPowerPairs_Type.__name__=_E
_LldpV2Xdot3RemPowerPairs_Object=MibTableColumn
lldpV2Xdot3RemPowerPairs=_LldpV2Xdot3RemPowerPairs_Object((1,3,111,2,802,3,1,5,1,3,2,1,5),_LldpV2Xdot3RemPowerPairs_Type())
lldpV2Xdot3RemPowerPairs.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPowerPairs.setStatus(_A)
class _LldpV2Xdot3RemPowerClass_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2),ValueRangeConstraint(3,3),ValueRangeConstraint(4,4),ValueRangeConstraint(5,5))
_LldpV2Xdot3RemPowerClass_Type.__name__=_E
_LldpV2Xdot3RemPowerClass_Object=MibTableColumn
lldpV2Xdot3RemPowerClass=_LldpV2Xdot3RemPowerClass_Object((1,3,111,2,802,3,1,5,1,3,2,1,6),_LldpV2Xdot3RemPowerClass_Type())
lldpV2Xdot3RemPowerClass.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPowerClass.setStatus(_A)
class _LldpV2Xdot3RemPowerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_O,0),(_P,1),(_Q,2),(_R,3)))
_LldpV2Xdot3RemPowerType_Type.__name__=_F
_LldpV2Xdot3RemPowerType_Object=MibTableColumn
lldpV2Xdot3RemPowerType=_LldpV2Xdot3RemPowerType_Object((1,3,111,2,802,3,1,5,1,3,2,1,7),_LldpV2Xdot3RemPowerType_Type())
lldpV2Xdot3RemPowerType.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPowerType.setStatus(_A)
class _LldpV2Xdot3RemPowerSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_S,0),(_T,1),(_U,2),(_V,3),('pdlocalonly',4),(_W,5),(_X,6)))
_LldpV2Xdot3RemPowerSource_Type.__name__=_F
_LldpV2Xdot3RemPowerSource_Object=MibTableColumn
lldpV2Xdot3RemPowerSource=_LldpV2Xdot3RemPowerSource_Object((1,3,111,2,802,3,1,5,1,3,2,1,8),_LldpV2Xdot3RemPowerSource_Type())
lldpV2Xdot3RemPowerSource.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPowerSource.setStatus(_A)
class _LldpV2Xdot3RemPowerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('low',0),('high',1),(_Y,2),(_Z,3)))
_LldpV2Xdot3RemPowerPriority_Type.__name__=_F
_LldpV2Xdot3RemPowerPriority_Object=MibTableColumn
lldpV2Xdot3RemPowerPriority=_LldpV2Xdot3RemPowerPriority_Object((1,3,111,2,802,3,1,5,1,3,2,1,9),_LldpV2Xdot3RemPowerPriority_Type())
lldpV2Xdot3RemPowerPriority.setMaxAccess(_M)
if mibBuilder.loadTexts:lldpV2Xdot3RemPowerPriority.setStatus(_A)
_LldpV2Xdot3RemPDRequestedPowerValue_Type=Integer32
_LldpV2Xdot3RemPDRequestedPowerValue_Object=MibTableColumn
lldpV2Xdot3RemPDRequestedPowerValue=_LldpV2Xdot3RemPDRequestedPowerValue_Object((1,3,111,2,802,3,1,5,1,3,2,1,10),_LldpV2Xdot3RemPDRequestedPowerValue_Type())
lldpV2Xdot3RemPDRequestedPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPDRequestedPowerValue.setStatus(_A)
_LldpV2Xdot3RemPSEAllocatedPowerValue_Type=Integer32
_LldpV2Xdot3RemPSEAllocatedPowerValue_Object=MibTableColumn
lldpV2Xdot3RemPSEAllocatedPowerValue=_LldpV2Xdot3RemPSEAllocatedPowerValue_Object((1,3,111,2,802,3,1,5,1,3,2,1,11),_LldpV2Xdot3RemPSEAllocatedPowerValue_Type())
lldpV2Xdot3RemPSEAllocatedPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPSEAllocatedPowerValue.setStatus(_A)
_LldpV2Xdot3RemMaxFrameSizeTable_Object=MibTable
lldpV2Xdot3RemMaxFrameSizeTable=_LldpV2Xdot3RemMaxFrameSizeTable_Object((1,3,111,2,802,3,1,5,1,3,3))
if mibBuilder.loadTexts:lldpV2Xdot3RemMaxFrameSizeTable.setStatus(_A)
_LldpV2Xdot3RemMaxFrameSizeEntry_Object=MibTableRow
lldpV2Xdot3RemMaxFrameSizeEntry=_LldpV2Xdot3RemMaxFrameSizeEntry_Object((1,3,111,2,802,3,1,5,1,3,3,1))
lldpV2Xdot3RemMaxFrameSizeEntry.setIndexNames((0,_D,_K),(0,_D,_H),(0,_D,_J),(0,_D,_I))
if mibBuilder.loadTexts:lldpV2Xdot3RemMaxFrameSizeEntry.setStatus(_A)
class _LldpV2Xdot3RemMaxFrameSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LldpV2Xdot3RemMaxFrameSize_Type.__name__=_E
_LldpV2Xdot3RemMaxFrameSize_Object=MibTableColumn
lldpV2Xdot3RemMaxFrameSize=_LldpV2Xdot3RemMaxFrameSize_Object((1,3,111,2,802,3,1,5,1,3,3,1,1),_LldpV2Xdot3RemMaxFrameSize_Type())
lldpV2Xdot3RemMaxFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemMaxFrameSize.setStatus(_A)
_LldpV2Xdot3RemEEETable_Object=MibTable
lldpV2Xdot3RemEEETable=_LldpV2Xdot3RemEEETable_Object((1,3,111,2,802,3,1,5,1,3,4))
if mibBuilder.loadTexts:lldpV2Xdot3RemEEETable.setStatus(_A)
_LldpV2Xdot3RemEEEEntry_Object=MibTableRow
lldpV2Xdot3RemEEEEntry=_LldpV2Xdot3RemEEEEntry_Object((1,3,111,2,802,3,1,5,1,3,4,1))
lldpV2Xdot3RemEEEEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:lldpV2Xdot3RemEEEEntry.setStatus(_A)
_LldpV2Xdot3RemTxTwSys_Type=Integer32
_LldpV2Xdot3RemTxTwSys_Object=MibTableColumn
lldpV2Xdot3RemTxTwSys=_LldpV2Xdot3RemTxTwSys_Object((1,3,111,2,802,3,1,5,1,3,4,1,1),_LldpV2Xdot3RemTxTwSys_Type())
lldpV2Xdot3RemTxTwSys.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemTxTwSys.setStatus(_A)
_LldpV2Xdot3RemTxTwSysEcho_Type=Integer32
_LldpV2Xdot3RemTxTwSysEcho_Object=MibTableColumn
lldpV2Xdot3RemTxTwSysEcho=_LldpV2Xdot3RemTxTwSysEcho_Object((1,3,111,2,802,3,1,5,1,3,4,1,2),_LldpV2Xdot3RemTxTwSysEcho_Type())
lldpV2Xdot3RemTxTwSysEcho.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemTxTwSysEcho.setStatus(_A)
_LldpV2Xdot3RemRxTwSys_Type=Integer32
_LldpV2Xdot3RemRxTwSys_Object=MibTableColumn
lldpV2Xdot3RemRxTwSys=_LldpV2Xdot3RemRxTwSys_Object((1,3,111,2,802,3,1,5,1,3,4,1,3),_LldpV2Xdot3RemRxTwSys_Type())
lldpV2Xdot3RemRxTwSys.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemRxTwSys.setStatus(_A)
_LldpV2Xdot3RemRxTwSysEcho_Type=Integer32
_LldpV2Xdot3RemRxTwSysEcho_Object=MibTableColumn
lldpV2Xdot3RemRxTwSysEcho=_LldpV2Xdot3RemRxTwSysEcho_Object((1,3,111,2,802,3,1,5,1,3,4,1,4),_LldpV2Xdot3RemRxTwSysEcho_Type())
lldpV2Xdot3RemRxTwSysEcho.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemRxTwSysEcho.setStatus(_A)
_LldpV2Xdot3RemFbTwSys_Type=Integer32
_LldpV2Xdot3RemFbTwSys_Object=MibTableColumn
lldpV2Xdot3RemFbTwSys=_LldpV2Xdot3RemFbTwSys_Object((1,3,111,2,802,3,1,5,1,3,4,1,5),_LldpV2Xdot3RemFbTwSys_Type())
lldpV2Xdot3RemFbTwSys.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemFbTwSys.setStatus(_A)
_LldpV2Xdot3Conformance_ObjectIdentity=ObjectIdentity
lldpV2Xdot3Conformance=_LldpV2Xdot3Conformance_ObjectIdentity((1,3,111,2,802,3,1,5,2))
_LldpV2Xdot3Compliances_ObjectIdentity=ObjectIdentity
lldpV2Xdot3Compliances=_LldpV2Xdot3Compliances_ObjectIdentity((1,3,111,2,802,3,1,5,2,1))
_LldpV2Xdot3Groups_ObjectIdentity=ObjectIdentity
lldpV2Xdot3Groups=_LldpV2Xdot3Groups_ObjectIdentity((1,3,111,2,802,3,1,5,2,2))
lldpV2PortConfigEntry.registerAugmentions((_B,_a))
lldpV2Xdot3PortConfigEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
lldpV2Xdot3ConfigGroup=ObjectGroup((1,3,111,2,802,3,1,5,2,2,1))
lldpV2Xdot3ConfigGroup.setObjects((_B,_b))
if mibBuilder.loadTexts:lldpV2Xdot3ConfigGroup.setStatus(_A)
lldpV2Xdot3LocSysGroup=ObjectGroup((1,3,111,2,802,3,1,5,2,2,2))
lldpV2Xdot3LocSysGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:lldpV2Xdot3LocSysGroup.setStatus(_A)
lldpV2Xdot3RemSysGroup=ObjectGroup((1,3,111,2,802,3,1,5,2,2,3))
lldpV2Xdot3RemSysGroup.setObjects(*((_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN)))
if mibBuilder.loadTexts:lldpV2Xdot3RemSysGroup.setStatus(_A)
lldpV2Xdot3TxRxCompliance=ModuleCompliance((1,3,111,2,802,3,1,5,2,1,1))
lldpV2Xdot3TxRxCompliance.setObjects(*((_B,_AO),(_B,_N)))
if mibBuilder.loadTexts:lldpV2Xdot3TxRxCompliance.setStatus(_A)
lldpV2Xdot3TxCompliance=ModuleCompliance((1,3,111,2,802,3,1,5,2,1,2))
lldpV2Xdot3TxCompliance.setObjects((_B,_AP))
if mibBuilder.loadTexts:lldpV2Xdot3TxCompliance.setStatus(_A)
lldpV2Xdot3RxCompliance=ModuleCompliance((1,3,111,2,802,3,1,5,2,1,3))
lldpV2Xdot3RxCompliance.setObjects((_B,_AQ))
if mibBuilder.loadTexts:lldpV2Xdot3RxCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ieee8023lldpV2Xdot3MIB':ieee8023lldpV2Xdot3MIB,'lldpV2Xdot3Objects':lldpV2Xdot3Objects,'lldpV2Xdot3Config':lldpV2Xdot3Config,'lldpV2Xdot3PortConfigTable':lldpV2Xdot3PortConfigTable,_a:lldpV2Xdot3PortConfigEntry,_b:lldpV2Xdot3PortConfigTLVsTxEnable,'lldpV2Xdot3LocalData':lldpV2Xdot3LocalData,'lldpV2Xdot3LocPortTable':lldpV2Xdot3LocPortTable,'lldpV2Xdot3LocPortEntry':lldpV2Xdot3LocPortEntry,_c:lldpV2Xdot3LocPortAutoNegSupported,_d:lldpV2Xdot3LocPortAutoNegEnabled,_e:lldpV2Xdot3LocPortAutoNegAdvertisedCap,_f:lldpV2Xdot3LocPortOperMauType,'lldpV2Xdot3LocPowerTable':lldpV2Xdot3LocPowerTable,'lldpV2Xdot3LocPowerEntry':lldpV2Xdot3LocPowerEntry,_g:lldpV2Xdot3LocPowerPortClass,_h:lldpV2Xdot3LocPowerMDISupported,_i:lldpV2Xdot3LocPowerMDIEnabled,_j:lldpV2Xdot3LocPowerPairControlable,_k:lldpV2Xdot3LocPowerPairs,_l:lldpV2Xdot3LocPowerClass,_n:lldpV2Xdot3LocPowerType,_o:lldpV2Xdot3LocPowerSource,_p:lldpV2Xdot3LocPowerPriority,_q:lldpV2Xdot3LocPDRequestedPowerValue,_r:lldpV2Xdot3LocPSEAllocatedPowerValue,_s:lldpV2Xdot3LocResponseTime,_t:lldpV2Xdot3LocReady,_u:lldpV2Xdot3LocReducedOperationPowerValue,'lldpV2Xdot3LocMaxFrameSizeTable':lldpV2Xdot3LocMaxFrameSizeTable,'lldpV2Xdot3LocMaxFrameSizeEntry':lldpV2Xdot3LocMaxFrameSizeEntry,_m:lldpV2Xdot3LocMaxFrameSize,'lldpV2Xdot3LocEEETable':lldpV2Xdot3LocEEETable,'lldpV2Xdot3LocEEEEntry':lldpV2Xdot3LocEEEEntry,_v:lldpV2Xdot3LocTxTwSys,_w:lldpV2Xdot3LocTxTwSysEcho,_x:lldpV2Xdot3LocRxTwSys,_y:lldpV2Xdot3LocRxTwSysEcho,_z:lldpV2Xdot3LocFbTwSys,_A0:lldpV2Xdot3TxDllReady,_A1:lldpV2Xdot3RxDllReady,_A2:lldpV2Xdot3LocDllEnabled,'lldpV2Xdot3RemoteData':lldpV2Xdot3RemoteData,'lldpV2Xdot3RemPortTable':lldpV2Xdot3RemPortTable,'lldpV2Xdot3RemPortEntry':lldpV2Xdot3RemPortEntry,_A3:lldpV2Xdot3RemPortAutoNegSupported,_A4:lldpV2Xdot3RemPortAutoNegEnabled,_A5:lldpV2Xdot3RemPortAutoNegAdvertisedCap,_A6:lldpV2Xdot3RemPortOperMauType,'lldpV2Xdot3RemPowerTable':lldpV2Xdot3RemPowerTable,'lldpV2Xdot3RemPowerEntry':lldpV2Xdot3RemPowerEntry,_A7:lldpV2Xdot3RemPowerPortClass,_A8:lldpV2Xdot3RemPowerMDISupported,_A9:lldpV2Xdot3RemPowerMDIEnabled,_AA:lldpV2Xdot3RemPowerPairControlable,_AB:lldpV2Xdot3RemPowerPairs,_AC:lldpV2Xdot3RemPowerClass,_AE:lldpV2Xdot3RemPowerType,_AF:lldpV2Xdot3RemPowerSource,_AG:lldpV2Xdot3RemPowerPriority,_AH:lldpV2Xdot3RemPDRequestedPowerValue,_AI:lldpV2Xdot3RemPSEAllocatedPowerValue,'lldpV2Xdot3RemMaxFrameSizeTable':lldpV2Xdot3RemMaxFrameSizeTable,'lldpV2Xdot3RemMaxFrameSizeEntry':lldpV2Xdot3RemMaxFrameSizeEntry,_AD:lldpV2Xdot3RemMaxFrameSize,'lldpV2Xdot3RemEEETable':lldpV2Xdot3RemEEETable,'lldpV2Xdot3RemEEEEntry':lldpV2Xdot3RemEEEEntry,_AJ:lldpV2Xdot3RemTxTwSys,_AK:lldpV2Xdot3RemTxTwSysEcho,_AL:lldpV2Xdot3RemRxTwSys,_AM:lldpV2Xdot3RemRxTwSysEcho,_AN:lldpV2Xdot3RemFbTwSys,'lldpV2Xdot3Conformance':lldpV2Xdot3Conformance,'lldpV2Xdot3Compliances':lldpV2Xdot3Compliances,'lldpV2Xdot3TxRxCompliance':lldpV2Xdot3TxRxCompliance,'lldpV2Xdot3TxCompliance':lldpV2Xdot3TxCompliance,'lldpV2Xdot3RxCompliance':lldpV2Xdot3RxCompliance,'lldpV2Xdot3Groups':lldpV2Xdot3Groups,_AO:lldpV2Xdot3ConfigGroup,_AP:lldpV2Xdot3LocSysGroup,_AQ:lldpV2Xdot3RemSysGroup})