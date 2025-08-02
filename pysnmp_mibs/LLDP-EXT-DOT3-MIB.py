_o='lldpXdot3RemSysGroup'
_n='lldpXdot3LocSysGroup'
_m='lldpXdot3ConfigGroup'
_l='lldpXdot3RemMaxFrameSize'
_k='lldpXdot3RemLinkAggPortId'
_j='lldpXdot3RemLinkAggStatus'
_i='lldpXdot3RemPowerClass'
_h='lldpXdot3RemPowerPairs'
_g='lldpXdot3RemPowerPairControlable'
_f='lldpXdot3RemPowerMDIEnabled'
_e='lldpXdot3RemPowerMDISupported'
_d='lldpXdot3RemPowerPortClass'
_c='lldpXdot3RemPortOperMauType'
_b='lldpXdot3RemPortAutoNegAdvertisedCap'
_a='lldpXdot3RemPortAutoNegEnabled'
_Z='lldpXdot3RemPortAutoNegSupported'
_Y='lldpXdot3LocMaxFrameSize'
_X='lldpXdot3LocLinkAggPortId'
_W='lldpXdot3LocLinkAggStatus'
_V='lldpXdot3LocPowerClass'
_U='lldpXdot3LocPowerPairs'
_T='lldpXdot3LocPowerPairControlable'
_S='lldpXdot3LocPowerMDIEnabled'
_R='lldpXdot3LocPowerMDISupported'
_Q='lldpXdot3LocPowerPortClass'
_P='lldpXdot3LocPortOperMauType'
_O='lldpXdot3LocPortAutoNegAdvertisedCap'
_N='lldpXdot3LocPortAutoNegEnabled'
_M='lldpXdot3LocPortAutoNegSupported'
_L='lldpXdot3PortConfigTLVsTxEnable'
_K='lldpXdot3PortConfigEntry'
_J='OctetString'
_I='lldpRemTimeMark'
_H='lldpRemLocalPortNum'
_G='lldpRemIndex'
_F='lldpLocPortNum'
_E='Integer32'
_D='LLDP-MIB'
_C='read-only'
_B='LLDP-EXT-DOT3-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lldpExtensions,lldpLocPortNum,lldpPortConfigEntry,lldpRemIndex,lldpRemLocalPortNum,lldpRemTimeMark=mibBuilder.importSymbols(_D,'lldpExtensions',_F,'lldpPortConfigEntry',_G,_H,_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
lldpXdot3MIB=ModuleIdentity((1,0,8802,1,1,2,1,5,4623))
if mibBuilder.loadTexts:lldpXdot3MIB.setRevisions(('2005-05-06 00:00',))
class LldpPowerPortClass(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pClassPSE',1),('pClassPD',2)))
class LldpLinkAggStatusMap(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('aggCapable',0),('aggEnabled',1)))
_LldpXdot3Objects_ObjectIdentity=ObjectIdentity
lldpXdot3Objects=_LldpXdot3Objects_ObjectIdentity((1,0,8802,1,1,2,1,5,4623,1))
_LldpXdot3Config_ObjectIdentity=ObjectIdentity
lldpXdot3Config=_LldpXdot3Config_ObjectIdentity((1,0,8802,1,1,2,1,5,4623,1,1))
_LldpXdot3PortConfigTable_Object=MibTable
lldpXdot3PortConfigTable=_LldpXdot3PortConfigTable_Object((1,0,8802,1,1,2,1,5,4623,1,1,1))
if mibBuilder.loadTexts:lldpXdot3PortConfigTable.setStatus(_A)
_LldpXdot3PortConfigEntry_Object=MibTableRow
lldpXdot3PortConfigEntry=_LldpXdot3PortConfigEntry_Object((1,0,8802,1,1,2,1,5,4623,1,1,1,1))
if mibBuilder.loadTexts:lldpXdot3PortConfigEntry.setStatus(_A)
class _LldpXdot3PortConfigTLVsTxEnable_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('macPhyConfigStatus',0),('powerViaMDI',1),('linkAggregation',2),('maxFrameSize',3)))
_LldpXdot3PortConfigTLVsTxEnable_Type.__name__='Bits'
_LldpXdot3PortConfigTLVsTxEnable_Object=MibTableColumn
lldpXdot3PortConfigTLVsTxEnable=_LldpXdot3PortConfigTLVsTxEnable_Object((1,0,8802,1,1,2,1,5,4623,1,1,1,1,1),_LldpXdot3PortConfigTLVsTxEnable_Type())
lldpXdot3PortConfigTLVsTxEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:lldpXdot3PortConfigTLVsTxEnable.setStatus(_A)
_LldpXdot3LocalData_ObjectIdentity=ObjectIdentity
lldpXdot3LocalData=_LldpXdot3LocalData_ObjectIdentity((1,0,8802,1,1,2,1,5,4623,1,2))
_LldpXdot3LocPortTable_Object=MibTable
lldpXdot3LocPortTable=_LldpXdot3LocPortTable_Object((1,0,8802,1,1,2,1,5,4623,1,2,1))
if mibBuilder.loadTexts:lldpXdot3LocPortTable.setStatus(_A)
_LldpXdot3LocPortEntry_Object=MibTableRow
lldpXdot3LocPortEntry=_LldpXdot3LocPortEntry_Object((1,0,8802,1,1,2,1,5,4623,1,2,1,1))
lldpXdot3LocPortEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:lldpXdot3LocPortEntry.setStatus(_A)
_LldpXdot3LocPortAutoNegSupported_Type=TruthValue
_LldpXdot3LocPortAutoNegSupported_Object=MibTableColumn
lldpXdot3LocPortAutoNegSupported=_LldpXdot3LocPortAutoNegSupported_Object((1,0,8802,1,1,2,1,5,4623,1,2,1,1,1),_LldpXdot3LocPortAutoNegSupported_Type())
lldpXdot3LocPortAutoNegSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3LocPortAutoNegSupported.setStatus(_A)
_LldpXdot3LocPortAutoNegEnabled_Type=TruthValue
_LldpXdot3LocPortAutoNegEnabled_Object=MibTableColumn
lldpXdot3LocPortAutoNegEnabled=_LldpXdot3LocPortAutoNegEnabled_Object((1,0,8802,1,1,2,1,5,4623,1,2,1,1,2),_LldpXdot3LocPortAutoNegEnabled_Type())
lldpXdot3LocPortAutoNegEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3LocPortAutoNegEnabled.setStatus(_A)
class _LldpXdot3LocPortAutoNegAdvertisedCap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_LldpXdot3LocPortAutoNegAdvertisedCap_Type.__name__=_J
_LldpXdot3LocPortAutoNegAdvertisedCap_Object=MibTableColumn
lldpXdot3LocPortAutoNegAdvertisedCap=_LldpXdot3LocPortAutoNegAdvertisedCap_Object((1,0,8802,1,1,2,1,5,4623,1,2,1,1,3),_LldpXdot3LocPortAutoNegAdvertisedCap_Type())
lldpXdot3LocPortAutoNegAdvertisedCap.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3LocPortAutoNegAdvertisedCap.setStatus(_A)
class _LldpXdot3LocPortOperMauType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_LldpXdot3LocPortOperMauType_Type.__name__=_E
_LldpXdot3LocPortOperMauType_Object=MibTableColumn
lldpXdot3LocPortOperMauType=_LldpXdot3LocPortOperMauType_Object((1,0,8802,1,1,2,1,5,4623,1,2,1,1,4),_LldpXdot3LocPortOperMauType_Type())
lldpXdot3LocPortOperMauType.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3LocPortOperMauType.setStatus(_A)
_LldpXdot3LocPowerTable_Object=MibTable
lldpXdot3LocPowerTable=_LldpXdot3LocPowerTable_Object((1,0,8802,1,1,2,1,5,4623,1,2,2))
if mibBuilder.loadTexts:lldpXdot3LocPowerTable.setStatus(_A)
_LldpXdot3LocPowerEntry_Object=MibTableRow
lldpXdot3LocPowerEntry=_LldpXdot3LocPowerEntry_Object((1,0,8802,1,1,2,1,5,4623,1,2,2,1))
lldpXdot3LocPowerEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:lldpXdot3LocPowerEntry.setStatus(_A)
_LldpXdot3LocPowerPortClass_Type=LldpPowerPortClass
_LldpXdot3LocPowerPortClass_Object=MibTableColumn
lldpXdot3LocPowerPortClass=_LldpXdot3LocPowerPortClass_Object((1,0,8802,1,1,2,1,5,4623,1,2,2,1,1),_LldpXdot3LocPowerPortClass_Type())
lldpXdot3LocPowerPortClass.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3LocPowerPortClass.setStatus(_A)
_LldpXdot3LocPowerMDISupported_Type=TruthValue
_LldpXdot3LocPowerMDISupported_Object=MibTableColumn
lldpXdot3LocPowerMDISupported=_LldpXdot3LocPowerMDISupported_Object((1,0,8802,1,1,2,1,5,4623,1,2,2,1,2),_LldpXdot3LocPowerMDISupported_Type())
lldpXdot3LocPowerMDISupported.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3LocPowerMDISupported.setStatus(_A)
_LldpXdot3LocPowerMDIEnabled_Type=TruthValue
_LldpXdot3LocPowerMDIEnabled_Object=MibTableColumn
lldpXdot3LocPowerMDIEnabled=_LldpXdot3LocPowerMDIEnabled_Object((1,0,8802,1,1,2,1,5,4623,1,2,2,1,3),_LldpXdot3LocPowerMDIEnabled_Type())
lldpXdot3LocPowerMDIEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3LocPowerMDIEnabled.setStatus(_A)
_LldpXdot3LocPowerPairControlable_Type=TruthValue
_LldpXdot3LocPowerPairControlable_Object=MibTableColumn
lldpXdot3LocPowerPairControlable=_LldpXdot3LocPowerPairControlable_Object((1,0,8802,1,1,2,1,5,4623,1,2,2,1,4),_LldpXdot3LocPowerPairControlable_Type())
lldpXdot3LocPowerPairControlable.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3LocPowerPairControlable.setStatus(_A)
class _LldpXdot3LocPowerPairs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_LldpXdot3LocPowerPairs_Type.__name__=_E
_LldpXdot3LocPowerPairs_Object=MibTableColumn
lldpXdot3LocPowerPairs=_LldpXdot3LocPowerPairs_Object((1,0,8802,1,1,2,1,5,4623,1,2,2,1,5),_LldpXdot3LocPowerPairs_Type())
lldpXdot3LocPowerPairs.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3LocPowerPairs.setStatus(_A)
class _LldpXdot3LocPowerClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2),ValueRangeConstraint(3,3),ValueRangeConstraint(4,4),ValueRangeConstraint(5,5))
_LldpXdot3LocPowerClass_Type.__name__=_E
_LldpXdot3LocPowerClass_Object=MibTableColumn
lldpXdot3LocPowerClass=_LldpXdot3LocPowerClass_Object((1,0,8802,1,1,2,1,5,4623,1,2,2,1,6),_LldpXdot3LocPowerClass_Type())
lldpXdot3LocPowerClass.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3LocPowerClass.setStatus(_A)
_LldpXdot3LocLinkAggTable_Object=MibTable
lldpXdot3LocLinkAggTable=_LldpXdot3LocLinkAggTable_Object((1,0,8802,1,1,2,1,5,4623,1,2,3))
if mibBuilder.loadTexts:lldpXdot3LocLinkAggTable.setStatus(_A)
_LldpXdot3LocLinkAggEntry_Object=MibTableRow
lldpXdot3LocLinkAggEntry=_LldpXdot3LocLinkAggEntry_Object((1,0,8802,1,1,2,1,5,4623,1,2,3,1))
lldpXdot3LocLinkAggEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:lldpXdot3LocLinkAggEntry.setStatus(_A)
_LldpXdot3LocLinkAggStatus_Type=LldpLinkAggStatusMap
_LldpXdot3LocLinkAggStatus_Object=MibTableColumn
lldpXdot3LocLinkAggStatus=_LldpXdot3LocLinkAggStatus_Object((1,0,8802,1,1,2,1,5,4623,1,2,3,1,1),_LldpXdot3LocLinkAggStatus_Type())
lldpXdot3LocLinkAggStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3LocLinkAggStatus.setStatus(_A)
class _LldpXdot3LocLinkAggPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_LldpXdot3LocLinkAggPortId_Type.__name__=_E
_LldpXdot3LocLinkAggPortId_Object=MibTableColumn
lldpXdot3LocLinkAggPortId=_LldpXdot3LocLinkAggPortId_Object((1,0,8802,1,1,2,1,5,4623,1,2,3,1,2),_LldpXdot3LocLinkAggPortId_Type())
lldpXdot3LocLinkAggPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3LocLinkAggPortId.setStatus(_A)
_LldpXdot3LocMaxFrameSizeTable_Object=MibTable
lldpXdot3LocMaxFrameSizeTable=_LldpXdot3LocMaxFrameSizeTable_Object((1,0,8802,1,1,2,1,5,4623,1,2,4))
if mibBuilder.loadTexts:lldpXdot3LocMaxFrameSizeTable.setStatus(_A)
_LldpXdot3LocMaxFrameSizeEntry_Object=MibTableRow
lldpXdot3LocMaxFrameSizeEntry=_LldpXdot3LocMaxFrameSizeEntry_Object((1,0,8802,1,1,2,1,5,4623,1,2,4,1))
lldpXdot3LocMaxFrameSizeEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:lldpXdot3LocMaxFrameSizeEntry.setStatus(_A)
class _LldpXdot3LocMaxFrameSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LldpXdot3LocMaxFrameSize_Type.__name__=_E
_LldpXdot3LocMaxFrameSize_Object=MibTableColumn
lldpXdot3LocMaxFrameSize=_LldpXdot3LocMaxFrameSize_Object((1,0,8802,1,1,2,1,5,4623,1,2,4,1,1),_LldpXdot3LocMaxFrameSize_Type())
lldpXdot3LocMaxFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3LocMaxFrameSize.setStatus(_A)
_LldpXdot3RemoteData_ObjectIdentity=ObjectIdentity
lldpXdot3RemoteData=_LldpXdot3RemoteData_ObjectIdentity((1,0,8802,1,1,2,1,5,4623,1,3))
_LldpXdot3RemPortTable_Object=MibTable
lldpXdot3RemPortTable=_LldpXdot3RemPortTable_Object((1,0,8802,1,1,2,1,5,4623,1,3,1))
if mibBuilder.loadTexts:lldpXdot3RemPortTable.setStatus(_A)
_LldpXdot3RemPortEntry_Object=MibTableRow
lldpXdot3RemPortEntry=_LldpXdot3RemPortEntry_Object((1,0,8802,1,1,2,1,5,4623,1,3,1,1))
lldpXdot3RemPortEntry.setIndexNames((0,_D,_I),(0,_D,_H),(0,_D,_G))
if mibBuilder.loadTexts:lldpXdot3RemPortEntry.setStatus(_A)
_LldpXdot3RemPortAutoNegSupported_Type=TruthValue
_LldpXdot3RemPortAutoNegSupported_Object=MibTableColumn
lldpXdot3RemPortAutoNegSupported=_LldpXdot3RemPortAutoNegSupported_Object((1,0,8802,1,1,2,1,5,4623,1,3,1,1,1),_LldpXdot3RemPortAutoNegSupported_Type())
lldpXdot3RemPortAutoNegSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3RemPortAutoNegSupported.setStatus(_A)
_LldpXdot3RemPortAutoNegEnabled_Type=TruthValue
_LldpXdot3RemPortAutoNegEnabled_Object=MibTableColumn
lldpXdot3RemPortAutoNegEnabled=_LldpXdot3RemPortAutoNegEnabled_Object((1,0,8802,1,1,2,1,5,4623,1,3,1,1,2),_LldpXdot3RemPortAutoNegEnabled_Type())
lldpXdot3RemPortAutoNegEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3RemPortAutoNegEnabled.setStatus(_A)
class _LldpXdot3RemPortAutoNegAdvertisedCap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_LldpXdot3RemPortAutoNegAdvertisedCap_Type.__name__=_J
_LldpXdot3RemPortAutoNegAdvertisedCap_Object=MibTableColumn
lldpXdot3RemPortAutoNegAdvertisedCap=_LldpXdot3RemPortAutoNegAdvertisedCap_Object((1,0,8802,1,1,2,1,5,4623,1,3,1,1,3),_LldpXdot3RemPortAutoNegAdvertisedCap_Type())
lldpXdot3RemPortAutoNegAdvertisedCap.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3RemPortAutoNegAdvertisedCap.setStatus(_A)
class _LldpXdot3RemPortOperMauType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_LldpXdot3RemPortOperMauType_Type.__name__=_E
_LldpXdot3RemPortOperMauType_Object=MibTableColumn
lldpXdot3RemPortOperMauType=_LldpXdot3RemPortOperMauType_Object((1,0,8802,1,1,2,1,5,4623,1,3,1,1,4),_LldpXdot3RemPortOperMauType_Type())
lldpXdot3RemPortOperMauType.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3RemPortOperMauType.setStatus(_A)
_LldpXdot3RemPowerTable_Object=MibTable
lldpXdot3RemPowerTable=_LldpXdot3RemPowerTable_Object((1,0,8802,1,1,2,1,5,4623,1,3,2))
if mibBuilder.loadTexts:lldpXdot3RemPowerTable.setStatus(_A)
_LldpXdot3RemPowerEntry_Object=MibTableRow
lldpXdot3RemPowerEntry=_LldpXdot3RemPowerEntry_Object((1,0,8802,1,1,2,1,5,4623,1,3,2,1))
lldpXdot3RemPowerEntry.setIndexNames((0,_D,_I),(0,_D,_H),(0,_D,_G))
if mibBuilder.loadTexts:lldpXdot3RemPowerEntry.setStatus(_A)
_LldpXdot3RemPowerPortClass_Type=LldpPowerPortClass
_LldpXdot3RemPowerPortClass_Object=MibTableColumn
lldpXdot3RemPowerPortClass=_LldpXdot3RemPowerPortClass_Object((1,0,8802,1,1,2,1,5,4623,1,3,2,1,1),_LldpXdot3RemPowerPortClass_Type())
lldpXdot3RemPowerPortClass.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3RemPowerPortClass.setStatus(_A)
_LldpXdot3RemPowerMDISupported_Type=TruthValue
_LldpXdot3RemPowerMDISupported_Object=MibTableColumn
lldpXdot3RemPowerMDISupported=_LldpXdot3RemPowerMDISupported_Object((1,0,8802,1,1,2,1,5,4623,1,3,2,1,2),_LldpXdot3RemPowerMDISupported_Type())
lldpXdot3RemPowerMDISupported.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3RemPowerMDISupported.setStatus(_A)
_LldpXdot3RemPowerMDIEnabled_Type=TruthValue
_LldpXdot3RemPowerMDIEnabled_Object=MibTableColumn
lldpXdot3RemPowerMDIEnabled=_LldpXdot3RemPowerMDIEnabled_Object((1,0,8802,1,1,2,1,5,4623,1,3,2,1,3),_LldpXdot3RemPowerMDIEnabled_Type())
lldpXdot3RemPowerMDIEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3RemPowerMDIEnabled.setStatus(_A)
_LldpXdot3RemPowerPairControlable_Type=TruthValue
_LldpXdot3RemPowerPairControlable_Object=MibTableColumn
lldpXdot3RemPowerPairControlable=_LldpXdot3RemPowerPairControlable_Object((1,0,8802,1,1,2,1,5,4623,1,3,2,1,4),_LldpXdot3RemPowerPairControlable_Type())
lldpXdot3RemPowerPairControlable.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3RemPowerPairControlable.setStatus(_A)
class _LldpXdot3RemPowerPairs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_LldpXdot3RemPowerPairs_Type.__name__=_E
_LldpXdot3RemPowerPairs_Object=MibTableColumn
lldpXdot3RemPowerPairs=_LldpXdot3RemPowerPairs_Object((1,0,8802,1,1,2,1,5,4623,1,3,2,1,5),_LldpXdot3RemPowerPairs_Type())
lldpXdot3RemPowerPairs.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3RemPowerPairs.setStatus(_A)
class _LldpXdot3RemPowerClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2),ValueRangeConstraint(3,3),ValueRangeConstraint(4,4),ValueRangeConstraint(5,5))
_LldpXdot3RemPowerClass_Type.__name__=_E
_LldpXdot3RemPowerClass_Object=MibTableColumn
lldpXdot3RemPowerClass=_LldpXdot3RemPowerClass_Object((1,0,8802,1,1,2,1,5,4623,1,3,2,1,6),_LldpXdot3RemPowerClass_Type())
lldpXdot3RemPowerClass.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3RemPowerClass.setStatus(_A)
_LldpXdot3RemLinkAggTable_Object=MibTable
lldpXdot3RemLinkAggTable=_LldpXdot3RemLinkAggTable_Object((1,0,8802,1,1,2,1,5,4623,1,3,3))
if mibBuilder.loadTexts:lldpXdot3RemLinkAggTable.setStatus(_A)
_LldpXdot3RemLinkAggEntry_Object=MibTableRow
lldpXdot3RemLinkAggEntry=_LldpXdot3RemLinkAggEntry_Object((1,0,8802,1,1,2,1,5,4623,1,3,3,1))
lldpXdot3RemLinkAggEntry.setIndexNames((0,_D,_I),(0,_D,_H),(0,_D,_G))
if mibBuilder.loadTexts:lldpXdot3RemLinkAggEntry.setStatus(_A)
_LldpXdot3RemLinkAggStatus_Type=LldpLinkAggStatusMap
_LldpXdot3RemLinkAggStatus_Object=MibTableColumn
lldpXdot3RemLinkAggStatus=_LldpXdot3RemLinkAggStatus_Object((1,0,8802,1,1,2,1,5,4623,1,3,3,1,1),_LldpXdot3RemLinkAggStatus_Type())
lldpXdot3RemLinkAggStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3RemLinkAggStatus.setStatus(_A)
class _LldpXdot3RemLinkAggPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_LldpXdot3RemLinkAggPortId_Type.__name__=_E
_LldpXdot3RemLinkAggPortId_Object=MibTableColumn
lldpXdot3RemLinkAggPortId=_LldpXdot3RemLinkAggPortId_Object((1,0,8802,1,1,2,1,5,4623,1,3,3,1,2),_LldpXdot3RemLinkAggPortId_Type())
lldpXdot3RemLinkAggPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3RemLinkAggPortId.setStatus(_A)
_LldpXdot3RemMaxFrameSizeTable_Object=MibTable
lldpXdot3RemMaxFrameSizeTable=_LldpXdot3RemMaxFrameSizeTable_Object((1,0,8802,1,1,2,1,5,4623,1,3,4))
if mibBuilder.loadTexts:lldpXdot3RemMaxFrameSizeTable.setStatus(_A)
_LldpXdot3RemMaxFrameSizeEntry_Object=MibTableRow
lldpXdot3RemMaxFrameSizeEntry=_LldpXdot3RemMaxFrameSizeEntry_Object((1,0,8802,1,1,2,1,5,4623,1,3,4,1))
lldpXdot3RemMaxFrameSizeEntry.setIndexNames((0,_D,_I),(0,_D,_H),(0,_D,_G))
if mibBuilder.loadTexts:lldpXdot3RemMaxFrameSizeEntry.setStatus(_A)
class _LldpXdot3RemMaxFrameSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LldpXdot3RemMaxFrameSize_Type.__name__=_E
_LldpXdot3RemMaxFrameSize_Object=MibTableColumn
lldpXdot3RemMaxFrameSize=_LldpXdot3RemMaxFrameSize_Object((1,0,8802,1,1,2,1,5,4623,1,3,4,1,1),_LldpXdot3RemMaxFrameSize_Type())
lldpXdot3RemMaxFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXdot3RemMaxFrameSize.setStatus(_A)
_LldpXdot3Conformance_ObjectIdentity=ObjectIdentity
lldpXdot3Conformance=_LldpXdot3Conformance_ObjectIdentity((1,0,8802,1,1,2,1,5,4623,2))
_LldpXdot3Compliances_ObjectIdentity=ObjectIdentity
lldpXdot3Compliances=_LldpXdot3Compliances_ObjectIdentity((1,0,8802,1,1,2,1,5,4623,2,1))
_LldpXdot3Groups_ObjectIdentity=ObjectIdentity
lldpXdot3Groups=_LldpXdot3Groups_ObjectIdentity((1,0,8802,1,1,2,1,5,4623,2,2))
lldpPortConfigEntry.registerAugmentions((_B,_K))
lldpXdot3PortConfigEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
lldpXdot3ConfigGroup=ObjectGroup((1,0,8802,1,1,2,1,5,4623,2,2,1))
lldpXdot3ConfigGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:lldpXdot3ConfigGroup.setStatus(_A)
lldpXdot3LocSysGroup=ObjectGroup((1,0,8802,1,1,2,1,5,4623,2,2,2))
lldpXdot3LocSysGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:lldpXdot3LocSysGroup.setStatus(_A)
lldpXdot3RemSysGroup=ObjectGroup((1,0,8802,1,1,2,1,5,4623,2,2,3))
lldpXdot3RemSysGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:lldpXdot3RemSysGroup.setStatus(_A)
lldpXdot3Compliance=ModuleCompliance((1,0,8802,1,1,2,1,5,4623,2,1,1))
lldpXdot3Compliance.setObjects(*((_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:lldpXdot3Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'LldpPowerPortClass':LldpPowerPortClass,'LldpLinkAggStatusMap':LldpLinkAggStatusMap,'lldpXdot3MIB':lldpXdot3MIB,'lldpXdot3Objects':lldpXdot3Objects,'lldpXdot3Config':lldpXdot3Config,'lldpXdot3PortConfigTable':lldpXdot3PortConfigTable,_K:lldpXdot3PortConfigEntry,_L:lldpXdot3PortConfigTLVsTxEnable,'lldpXdot3LocalData':lldpXdot3LocalData,'lldpXdot3LocPortTable':lldpXdot3LocPortTable,'lldpXdot3LocPortEntry':lldpXdot3LocPortEntry,_M:lldpXdot3LocPortAutoNegSupported,_N:lldpXdot3LocPortAutoNegEnabled,_O:lldpXdot3LocPortAutoNegAdvertisedCap,_P:lldpXdot3LocPortOperMauType,'lldpXdot3LocPowerTable':lldpXdot3LocPowerTable,'lldpXdot3LocPowerEntry':lldpXdot3LocPowerEntry,_Q:lldpXdot3LocPowerPortClass,_R:lldpXdot3LocPowerMDISupported,_S:lldpXdot3LocPowerMDIEnabled,_T:lldpXdot3LocPowerPairControlable,_U:lldpXdot3LocPowerPairs,_V:lldpXdot3LocPowerClass,'lldpXdot3LocLinkAggTable':lldpXdot3LocLinkAggTable,'lldpXdot3LocLinkAggEntry':lldpXdot3LocLinkAggEntry,_W:lldpXdot3LocLinkAggStatus,_X:lldpXdot3LocLinkAggPortId,'lldpXdot3LocMaxFrameSizeTable':lldpXdot3LocMaxFrameSizeTable,'lldpXdot3LocMaxFrameSizeEntry':lldpXdot3LocMaxFrameSizeEntry,_Y:lldpXdot3LocMaxFrameSize,'lldpXdot3RemoteData':lldpXdot3RemoteData,'lldpXdot3RemPortTable':lldpXdot3RemPortTable,'lldpXdot3RemPortEntry':lldpXdot3RemPortEntry,_Z:lldpXdot3RemPortAutoNegSupported,_a:lldpXdot3RemPortAutoNegEnabled,_b:lldpXdot3RemPortAutoNegAdvertisedCap,_c:lldpXdot3RemPortOperMauType,'lldpXdot3RemPowerTable':lldpXdot3RemPowerTable,'lldpXdot3RemPowerEntry':lldpXdot3RemPowerEntry,_d:lldpXdot3RemPowerPortClass,_e:lldpXdot3RemPowerMDISupported,_f:lldpXdot3RemPowerMDIEnabled,_g:lldpXdot3RemPowerPairControlable,_h:lldpXdot3RemPowerPairs,_i:lldpXdot3RemPowerClass,'lldpXdot3RemLinkAggTable':lldpXdot3RemLinkAggTable,'lldpXdot3RemLinkAggEntry':lldpXdot3RemLinkAggEntry,_j:lldpXdot3RemLinkAggStatus,_k:lldpXdot3RemLinkAggPortId,'lldpXdot3RemMaxFrameSizeTable':lldpXdot3RemMaxFrameSizeTable,'lldpXdot3RemMaxFrameSizeEntry':lldpXdot3RemMaxFrameSizeEntry,_l:lldpXdot3RemMaxFrameSize,'lldpXdot3Conformance':lldpXdot3Conformance,'lldpXdot3Compliances':lldpXdot3Compliances,'lldpXdot3Compliance':lldpXdot3Compliance,'lldpXdot3Groups':lldpXdot3Groups,_m:lldpXdot3ConfigGroup,_n:lldpXdot3LocSysGroup,_o:lldpXdot3RemSysGroup})