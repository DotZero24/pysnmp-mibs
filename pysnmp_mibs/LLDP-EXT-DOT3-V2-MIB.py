_m='lldpV2Xdot3RemSysGroup'
_l='lldpV2Xdot3LocSysGroup'
_k='lldpV2Xdot3ConfigGroup'
_j='lldpV2Xdot3RemMaxFrameSize'
_i='lldpV2Xdot3RemPowerClass'
_h='lldpV2Xdot3RemPowerPairs'
_g='lldpV2Xdot3RemPowerPairControlable'
_f='lldpV2Xdot3RemPowerMDIEnabled'
_e='lldpV2Xdot3RemPowerMDISupported'
_d='lldpV2Xdot3RemPowerPortClass'
_c='lldpV2Xdot3RemPortOperMauType'
_b='lldpV2Xdot3RemPortAutoNegAdvertisedCap'
_a='lldpV2Xdot3RemPortAutoNegEnabled'
_Z='lldpV2Xdot3RemPortAutoNegSupported'
_Y='lldpV2Xdot3LocMaxFrameSize'
_X='lldpV2Xdot3LocPowerClass'
_W='lldpV2Xdot3LocPowerPairs'
_V='lldpV2Xdot3LocPowerPairControlable'
_U='lldpV2Xdot3LocPowerMDIEnabled'
_T='lldpV2Xdot3LocPowerMDISupported'
_S='lldpV2Xdot3LocPowerPortClass'
_R='lldpV2Xdot3LocPortOperMauType'
_Q='lldpV2Xdot3LocPortAutoNegAdvertisedCap'
_P='lldpV2Xdot3LocPortAutoNegEnabled'
_O='lldpV2Xdot3LocPortAutoNegSupported'
_N='lldpV2Xdot3PortConfigTLVsTxEnable'
_M='lldpV2Xdot3PortConfigEntry'
_L='ifGeneralInformationGroup'
_K='OctetString'
_J='lldpV2RemTimeMark'
_I='lldpV2RemLocalIfIndex'
_H='lldpV2RemLocalDestMACAddress'
_G='lldpV2RemIndex'
_F='lldpV2LocPortIfIndex'
_E='Unsigned32'
_D='LLDP-V2-MIB'
_C='read-only'
_B='LLDP-EXT-DOT3-V2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifGeneralInformationGroup,=mibBuilder.importSymbols('IF-MIB',_L)
lldpV2Extensions,lldpV2LocPortIfIndex,lldpV2PortConfigEntry,lldpV2RemIndex,lldpV2RemLocalDestMACAddress,lldpV2RemLocalIfIndex,lldpV2RemTimeMark=mibBuilder.importSymbols(_D,'lldpV2Extensions',_F,'lldpV2PortConfigEntry',_G,_H,_I,_J)
LldpV2PowerPortClass,=mibBuilder.importSymbols('LLDP-V2-TC-MIB','LldpV2PowerPortClass')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
lldpV2Xdot3MIB=ModuleIdentity((1,3,111,2,802,1,1,13,1,5,4623))
if mibBuilder.loadTexts:lldpV2Xdot3MIB.setRevisions(('2009-06-08 00:00',))
_LldpV2Xdot3Objects_ObjectIdentity=ObjectIdentity
lldpV2Xdot3Objects=_LldpV2Xdot3Objects_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,4623,1))
_LldpV2Xdot3Config_ObjectIdentity=ObjectIdentity
lldpV2Xdot3Config=_LldpV2Xdot3Config_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,4623,1,1))
_LldpV2Xdot3PortConfigTable_Object=MibTable
lldpV2Xdot3PortConfigTable=_LldpV2Xdot3PortConfigTable_Object((1,3,111,2,802,1,1,13,1,5,4623,1,1,1))
if mibBuilder.loadTexts:lldpV2Xdot3PortConfigTable.setStatus(_A)
_LldpV2Xdot3PortConfigEntry_Object=MibTableRow
lldpV2Xdot3PortConfigEntry=_LldpV2Xdot3PortConfigEntry_Object((1,3,111,2,802,1,1,13,1,5,4623,1,1,1,1))
if mibBuilder.loadTexts:lldpV2Xdot3PortConfigEntry.setStatus(_A)
class _LldpV2Xdot3PortConfigTLVsTxEnable_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('macPhyConfigStatus',0),('powerViaMDI',1),('unused',2),('maxFrameSize',3)))
_LldpV2Xdot3PortConfigTLVsTxEnable_Type.__name__='Bits'
_LldpV2Xdot3PortConfigTLVsTxEnable_Object=MibTableColumn
lldpV2Xdot3PortConfigTLVsTxEnable=_LldpV2Xdot3PortConfigTLVsTxEnable_Object((1,3,111,2,802,1,1,13,1,5,4623,1,1,1,1,1),_LldpV2Xdot3PortConfigTLVsTxEnable_Type())
lldpV2Xdot3PortConfigTLVsTxEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:lldpV2Xdot3PortConfigTLVsTxEnable.setStatus(_A)
_LldpV2Xdot3LocalData_ObjectIdentity=ObjectIdentity
lldpV2Xdot3LocalData=_LldpV2Xdot3LocalData_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,4623,1,2))
_LldpV2Xdot3LocPortTable_Object=MibTable
lldpV2Xdot3LocPortTable=_LldpV2Xdot3LocPortTable_Object((1,3,111,2,802,1,1,13,1,5,4623,1,2,1))
if mibBuilder.loadTexts:lldpV2Xdot3LocPortTable.setStatus(_A)
_LldpV2Xdot3LocPortEntry_Object=MibTableRow
lldpV2Xdot3LocPortEntry=_LldpV2Xdot3LocPortEntry_Object((1,3,111,2,802,1,1,13,1,5,4623,1,2,1,1))
lldpV2Xdot3LocPortEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:lldpV2Xdot3LocPortEntry.setStatus(_A)
_LldpV2Xdot3LocPortAutoNegSupported_Type=TruthValue
_LldpV2Xdot3LocPortAutoNegSupported_Object=MibTableColumn
lldpV2Xdot3LocPortAutoNegSupported=_LldpV2Xdot3LocPortAutoNegSupported_Object((1,3,111,2,802,1,1,13,1,5,4623,1,2,1,1,1),_LldpV2Xdot3LocPortAutoNegSupported_Type())
lldpV2Xdot3LocPortAutoNegSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPortAutoNegSupported.setStatus(_A)
_LldpV2Xdot3LocPortAutoNegEnabled_Type=TruthValue
_LldpV2Xdot3LocPortAutoNegEnabled_Object=MibTableColumn
lldpV2Xdot3LocPortAutoNegEnabled=_LldpV2Xdot3LocPortAutoNegEnabled_Object((1,3,111,2,802,1,1,13,1,5,4623,1,2,1,1,2),_LldpV2Xdot3LocPortAutoNegEnabled_Type())
lldpV2Xdot3LocPortAutoNegEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPortAutoNegEnabled.setStatus(_A)
class _LldpV2Xdot3LocPortAutoNegAdvertisedCap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_LldpV2Xdot3LocPortAutoNegAdvertisedCap_Type.__name__=_K
_LldpV2Xdot3LocPortAutoNegAdvertisedCap_Object=MibTableColumn
lldpV2Xdot3LocPortAutoNegAdvertisedCap=_LldpV2Xdot3LocPortAutoNegAdvertisedCap_Object((1,3,111,2,802,1,1,13,1,5,4623,1,2,1,1,3),_LldpV2Xdot3LocPortAutoNegAdvertisedCap_Type())
lldpV2Xdot3LocPortAutoNegAdvertisedCap.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPortAutoNegAdvertisedCap.setStatus(_A)
class _LldpV2Xdot3LocPortOperMauType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_LldpV2Xdot3LocPortOperMauType_Type.__name__=_E
_LldpV2Xdot3LocPortOperMauType_Object=MibTableColumn
lldpV2Xdot3LocPortOperMauType=_LldpV2Xdot3LocPortOperMauType_Object((1,3,111,2,802,1,1,13,1,5,4623,1,2,1,1,4),_LldpV2Xdot3LocPortOperMauType_Type())
lldpV2Xdot3LocPortOperMauType.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPortOperMauType.setStatus(_A)
_LldpV2Xdot3LocPowerTable_Object=MibTable
lldpV2Xdot3LocPowerTable=_LldpV2Xdot3LocPowerTable_Object((1,3,111,2,802,1,1,13,1,5,4623,1,2,2))
if mibBuilder.loadTexts:lldpV2Xdot3LocPowerTable.setStatus(_A)
_LldpV2Xdot3LocPowerEntry_Object=MibTableRow
lldpV2Xdot3LocPowerEntry=_LldpV2Xdot3LocPowerEntry_Object((1,3,111,2,802,1,1,13,1,5,4623,1,2,2,1))
lldpV2Xdot3LocPowerEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:lldpV2Xdot3LocPowerEntry.setStatus(_A)
_LldpV2Xdot3LocPowerPortClass_Type=LldpV2PowerPortClass
_LldpV2Xdot3LocPowerPortClass_Object=MibTableColumn
lldpV2Xdot3LocPowerPortClass=_LldpV2Xdot3LocPowerPortClass_Object((1,3,111,2,802,1,1,13,1,5,4623,1,2,2,1,1),_LldpV2Xdot3LocPowerPortClass_Type())
lldpV2Xdot3LocPowerPortClass.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPowerPortClass.setStatus(_A)
_LldpV2Xdot3LocPowerMDISupported_Type=TruthValue
_LldpV2Xdot3LocPowerMDISupported_Object=MibTableColumn
lldpV2Xdot3LocPowerMDISupported=_LldpV2Xdot3LocPowerMDISupported_Object((1,3,111,2,802,1,1,13,1,5,4623,1,2,2,1,2),_LldpV2Xdot3LocPowerMDISupported_Type())
lldpV2Xdot3LocPowerMDISupported.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPowerMDISupported.setStatus(_A)
_LldpV2Xdot3LocPowerMDIEnabled_Type=TruthValue
_LldpV2Xdot3LocPowerMDIEnabled_Object=MibTableColumn
lldpV2Xdot3LocPowerMDIEnabled=_LldpV2Xdot3LocPowerMDIEnabled_Object((1,3,111,2,802,1,1,13,1,5,4623,1,2,2,1,3),_LldpV2Xdot3LocPowerMDIEnabled_Type())
lldpV2Xdot3LocPowerMDIEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPowerMDIEnabled.setStatus(_A)
_LldpV2Xdot3LocPowerPairControlable_Type=TruthValue
_LldpV2Xdot3LocPowerPairControlable_Object=MibTableColumn
lldpV2Xdot3LocPowerPairControlable=_LldpV2Xdot3LocPowerPairControlable_Object((1,3,111,2,802,1,1,13,1,5,4623,1,2,2,1,4),_LldpV2Xdot3LocPowerPairControlable_Type())
lldpV2Xdot3LocPowerPairControlable.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPowerPairControlable.setStatus(_A)
class _LldpV2Xdot3LocPowerPairs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_LldpV2Xdot3LocPowerPairs_Type.__name__=_E
_LldpV2Xdot3LocPowerPairs_Object=MibTableColumn
lldpV2Xdot3LocPowerPairs=_LldpV2Xdot3LocPowerPairs_Object((1,3,111,2,802,1,1,13,1,5,4623,1,2,2,1,5),_LldpV2Xdot3LocPowerPairs_Type())
lldpV2Xdot3LocPowerPairs.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPowerPairs.setStatus(_A)
class _LldpV2Xdot3LocPowerClass_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2),ValueRangeConstraint(3,3),ValueRangeConstraint(4,4),ValueRangeConstraint(5,5))
_LldpV2Xdot3LocPowerClass_Type.__name__=_E
_LldpV2Xdot3LocPowerClass_Object=MibTableColumn
lldpV2Xdot3LocPowerClass=_LldpV2Xdot3LocPowerClass_Object((1,3,111,2,802,1,1,13,1,5,4623,1,2,2,1,6),_LldpV2Xdot3LocPowerClass_Type())
lldpV2Xdot3LocPowerClass.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocPowerClass.setStatus(_A)
_LldpV2Xdot3LocMaxFrameSizeTable_Object=MibTable
lldpV2Xdot3LocMaxFrameSizeTable=_LldpV2Xdot3LocMaxFrameSizeTable_Object((1,3,111,2,802,1,1,13,1,5,4623,1,2,3))
if mibBuilder.loadTexts:lldpV2Xdot3LocMaxFrameSizeTable.setStatus(_A)
_LldpV2Xdot3LocMaxFrameSizeEntry_Object=MibTableRow
lldpV2Xdot3LocMaxFrameSizeEntry=_LldpV2Xdot3LocMaxFrameSizeEntry_Object((1,3,111,2,802,1,1,13,1,5,4623,1,2,3,1))
lldpV2Xdot3LocMaxFrameSizeEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:lldpV2Xdot3LocMaxFrameSizeEntry.setStatus(_A)
class _LldpV2Xdot3LocMaxFrameSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LldpV2Xdot3LocMaxFrameSize_Type.__name__=_E
_LldpV2Xdot3LocMaxFrameSize_Object=MibTableColumn
lldpV2Xdot3LocMaxFrameSize=_LldpV2Xdot3LocMaxFrameSize_Object((1,3,111,2,802,1,1,13,1,5,4623,1,2,3,1,1),_LldpV2Xdot3LocMaxFrameSize_Type())
lldpV2Xdot3LocMaxFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3LocMaxFrameSize.setStatus(_A)
_LldpV2Xdot3RemoteData_ObjectIdentity=ObjectIdentity
lldpV2Xdot3RemoteData=_LldpV2Xdot3RemoteData_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,4623,1,3))
_LldpV2Xdot3RemPortTable_Object=MibTable
lldpV2Xdot3RemPortTable=_LldpV2Xdot3RemPortTable_Object((1,3,111,2,802,1,1,13,1,5,4623,1,3,1))
if mibBuilder.loadTexts:lldpV2Xdot3RemPortTable.setStatus(_A)
_LldpV2Xdot3RemPortEntry_Object=MibTableRow
lldpV2Xdot3RemPortEntry=_LldpV2Xdot3RemPortEntry_Object((1,3,111,2,802,1,1,13,1,5,4623,1,3,1,1))
lldpV2Xdot3RemPortEntry.setIndexNames((0,_D,_J),(0,_D,_I),(0,_D,_H),(0,_D,_G))
if mibBuilder.loadTexts:lldpV2Xdot3RemPortEntry.setStatus(_A)
_LldpV2Xdot3RemPortAutoNegSupported_Type=TruthValue
_LldpV2Xdot3RemPortAutoNegSupported_Object=MibTableColumn
lldpV2Xdot3RemPortAutoNegSupported=_LldpV2Xdot3RemPortAutoNegSupported_Object((1,3,111,2,802,1,1,13,1,5,4623,1,3,1,1,1),_LldpV2Xdot3RemPortAutoNegSupported_Type())
lldpV2Xdot3RemPortAutoNegSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPortAutoNegSupported.setStatus(_A)
_LldpV2Xdot3RemPortAutoNegEnabled_Type=TruthValue
_LldpV2Xdot3RemPortAutoNegEnabled_Object=MibTableColumn
lldpV2Xdot3RemPortAutoNegEnabled=_LldpV2Xdot3RemPortAutoNegEnabled_Object((1,3,111,2,802,1,1,13,1,5,4623,1,3,1,1,2),_LldpV2Xdot3RemPortAutoNegEnabled_Type())
lldpV2Xdot3RemPortAutoNegEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPortAutoNegEnabled.setStatus(_A)
class _LldpV2Xdot3RemPortAutoNegAdvertisedCap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_LldpV2Xdot3RemPortAutoNegAdvertisedCap_Type.__name__=_K
_LldpV2Xdot3RemPortAutoNegAdvertisedCap_Object=MibTableColumn
lldpV2Xdot3RemPortAutoNegAdvertisedCap=_LldpV2Xdot3RemPortAutoNegAdvertisedCap_Object((1,3,111,2,802,1,1,13,1,5,4623,1,3,1,1,3),_LldpV2Xdot3RemPortAutoNegAdvertisedCap_Type())
lldpV2Xdot3RemPortAutoNegAdvertisedCap.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPortAutoNegAdvertisedCap.setStatus(_A)
class _LldpV2Xdot3RemPortOperMauType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_LldpV2Xdot3RemPortOperMauType_Type.__name__=_E
_LldpV2Xdot3RemPortOperMauType_Object=MibTableColumn
lldpV2Xdot3RemPortOperMauType=_LldpV2Xdot3RemPortOperMauType_Object((1,3,111,2,802,1,1,13,1,5,4623,1,3,1,1,4),_LldpV2Xdot3RemPortOperMauType_Type())
lldpV2Xdot3RemPortOperMauType.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPortOperMauType.setStatus(_A)
_LldpV2Xdot3RemPowerTable_Object=MibTable
lldpV2Xdot3RemPowerTable=_LldpV2Xdot3RemPowerTable_Object((1,3,111,2,802,1,1,13,1,5,4623,1,3,2))
if mibBuilder.loadTexts:lldpV2Xdot3RemPowerTable.setStatus(_A)
_LldpV2Xdot3RemPowerEntry_Object=MibTableRow
lldpV2Xdot3RemPowerEntry=_LldpV2Xdot3RemPowerEntry_Object((1,3,111,2,802,1,1,13,1,5,4623,1,3,2,1))
lldpV2Xdot3RemPowerEntry.setIndexNames((0,_D,_J),(0,_D,_I),(0,_D,_H),(0,_D,_G))
if mibBuilder.loadTexts:lldpV2Xdot3RemPowerEntry.setStatus(_A)
_LldpV2Xdot3RemPowerPortClass_Type=LldpV2PowerPortClass
_LldpV2Xdot3RemPowerPortClass_Object=MibTableColumn
lldpV2Xdot3RemPowerPortClass=_LldpV2Xdot3RemPowerPortClass_Object((1,3,111,2,802,1,1,13,1,5,4623,1,3,2,1,1),_LldpV2Xdot3RemPowerPortClass_Type())
lldpV2Xdot3RemPowerPortClass.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPowerPortClass.setStatus(_A)
_LldpV2Xdot3RemPowerMDISupported_Type=TruthValue
_LldpV2Xdot3RemPowerMDISupported_Object=MibTableColumn
lldpV2Xdot3RemPowerMDISupported=_LldpV2Xdot3RemPowerMDISupported_Object((1,3,111,2,802,1,1,13,1,5,4623,1,3,2,1,2),_LldpV2Xdot3RemPowerMDISupported_Type())
lldpV2Xdot3RemPowerMDISupported.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPowerMDISupported.setStatus(_A)
_LldpV2Xdot3RemPowerMDIEnabled_Type=TruthValue
_LldpV2Xdot3RemPowerMDIEnabled_Object=MibTableColumn
lldpV2Xdot3RemPowerMDIEnabled=_LldpV2Xdot3RemPowerMDIEnabled_Object((1,3,111,2,802,1,1,13,1,5,4623,1,3,2,1,3),_LldpV2Xdot3RemPowerMDIEnabled_Type())
lldpV2Xdot3RemPowerMDIEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPowerMDIEnabled.setStatus(_A)
_LldpV2Xdot3RemPowerPairControlable_Type=TruthValue
_LldpV2Xdot3RemPowerPairControlable_Object=MibTableColumn
lldpV2Xdot3RemPowerPairControlable=_LldpV2Xdot3RemPowerPairControlable_Object((1,3,111,2,802,1,1,13,1,5,4623,1,3,2,1,4),_LldpV2Xdot3RemPowerPairControlable_Type())
lldpV2Xdot3RemPowerPairControlable.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPowerPairControlable.setStatus(_A)
class _LldpV2Xdot3RemPowerPairs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_LldpV2Xdot3RemPowerPairs_Type.__name__=_E
_LldpV2Xdot3RemPowerPairs_Object=MibTableColumn
lldpV2Xdot3RemPowerPairs=_LldpV2Xdot3RemPowerPairs_Object((1,3,111,2,802,1,1,13,1,5,4623,1,3,2,1,5),_LldpV2Xdot3RemPowerPairs_Type())
lldpV2Xdot3RemPowerPairs.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPowerPairs.setStatus(_A)
class _LldpV2Xdot3RemPowerClass_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2),ValueRangeConstraint(3,3),ValueRangeConstraint(4,4),ValueRangeConstraint(5,5))
_LldpV2Xdot3RemPowerClass_Type.__name__=_E
_LldpV2Xdot3RemPowerClass_Object=MibTableColumn
lldpV2Xdot3RemPowerClass=_LldpV2Xdot3RemPowerClass_Object((1,3,111,2,802,1,1,13,1,5,4623,1,3,2,1,6),_LldpV2Xdot3RemPowerClass_Type())
lldpV2Xdot3RemPowerClass.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemPowerClass.setStatus(_A)
_LldpV2Xdot3RemMaxFrameSizeTable_Object=MibTable
lldpV2Xdot3RemMaxFrameSizeTable=_LldpV2Xdot3RemMaxFrameSizeTable_Object((1,3,111,2,802,1,1,13,1,5,4623,1,3,3))
if mibBuilder.loadTexts:lldpV2Xdot3RemMaxFrameSizeTable.setStatus(_A)
_LldpV2Xdot3RemMaxFrameSizeEntry_Object=MibTableRow
lldpV2Xdot3RemMaxFrameSizeEntry=_LldpV2Xdot3RemMaxFrameSizeEntry_Object((1,3,111,2,802,1,1,13,1,5,4623,1,3,3,1))
lldpV2Xdot3RemMaxFrameSizeEntry.setIndexNames((0,_D,_J),(0,_D,_I),(0,_D,_H),(0,_D,_G))
if mibBuilder.loadTexts:lldpV2Xdot3RemMaxFrameSizeEntry.setStatus(_A)
class _LldpV2Xdot3RemMaxFrameSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LldpV2Xdot3RemMaxFrameSize_Type.__name__=_E
_LldpV2Xdot3RemMaxFrameSize_Object=MibTableColumn
lldpV2Xdot3RemMaxFrameSize=_LldpV2Xdot3RemMaxFrameSize_Object((1,3,111,2,802,1,1,13,1,5,4623,1,3,3,1,1),_LldpV2Xdot3RemMaxFrameSize_Type())
lldpV2Xdot3RemMaxFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpV2Xdot3RemMaxFrameSize.setStatus(_A)
_LldpV2Xdot3Conformance_ObjectIdentity=ObjectIdentity
lldpV2Xdot3Conformance=_LldpV2Xdot3Conformance_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,4623,2))
_LldpV2Xdot3Compliances_ObjectIdentity=ObjectIdentity
lldpV2Xdot3Compliances=_LldpV2Xdot3Compliances_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,4623,2,1))
_LldpV2Xdot3Groups_ObjectIdentity=ObjectIdentity
lldpV2Xdot3Groups=_LldpV2Xdot3Groups_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,4623,2,2))
lldpV2PortConfigEntry.registerAugmentions((_B,_M))
lldpV2Xdot3PortConfigEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
lldpV2Xdot3ConfigGroup=ObjectGroup((1,3,111,2,802,1,1,13,1,5,4623,2,2,1))
lldpV2Xdot3ConfigGroup.setObjects((_B,_N))
if mibBuilder.loadTexts:lldpV2Xdot3ConfigGroup.setStatus(_A)
lldpV2Xdot3LocSysGroup=ObjectGroup((1,3,111,2,802,1,1,13,1,5,4623,2,2,2))
lldpV2Xdot3LocSysGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:lldpV2Xdot3LocSysGroup.setStatus(_A)
lldpV2Xdot3RemSysGroup=ObjectGroup((1,3,111,2,802,1,1,13,1,5,4623,2,2,3))
lldpV2Xdot3RemSysGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:lldpV2Xdot3RemSysGroup.setStatus(_A)
lldpV2Xdot3TxRxCompliance=ModuleCompliance((1,3,111,2,802,1,1,13,1,5,4623,2,1,1))
lldpV2Xdot3TxRxCompliance.setObjects(*((_B,_k),(_B,_L)))
if mibBuilder.loadTexts:lldpV2Xdot3TxRxCompliance.setStatus(_A)
lldpV2Xdot3TxCompliance=ModuleCompliance((1,3,111,2,802,1,1,13,1,5,4623,2,1,2))
lldpV2Xdot3TxCompliance.setObjects((_B,_l))
if mibBuilder.loadTexts:lldpV2Xdot3TxCompliance.setStatus(_A)
lldpV2Xdot3RxCompliance=ModuleCompliance((1,3,111,2,802,1,1,13,1,5,4623,2,1,3))
lldpV2Xdot3RxCompliance.setObjects((_B,_m))
if mibBuilder.loadTexts:lldpV2Xdot3RxCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lldpV2Xdot3MIB':lldpV2Xdot3MIB,'lldpV2Xdot3Objects':lldpV2Xdot3Objects,'lldpV2Xdot3Config':lldpV2Xdot3Config,'lldpV2Xdot3PortConfigTable':lldpV2Xdot3PortConfigTable,_M:lldpV2Xdot3PortConfigEntry,_N:lldpV2Xdot3PortConfigTLVsTxEnable,'lldpV2Xdot3LocalData':lldpV2Xdot3LocalData,'lldpV2Xdot3LocPortTable':lldpV2Xdot3LocPortTable,'lldpV2Xdot3LocPortEntry':lldpV2Xdot3LocPortEntry,_O:lldpV2Xdot3LocPortAutoNegSupported,_P:lldpV2Xdot3LocPortAutoNegEnabled,_Q:lldpV2Xdot3LocPortAutoNegAdvertisedCap,_R:lldpV2Xdot3LocPortOperMauType,'lldpV2Xdot3LocPowerTable':lldpV2Xdot3LocPowerTable,'lldpV2Xdot3LocPowerEntry':lldpV2Xdot3LocPowerEntry,_S:lldpV2Xdot3LocPowerPortClass,_T:lldpV2Xdot3LocPowerMDISupported,_U:lldpV2Xdot3LocPowerMDIEnabled,_V:lldpV2Xdot3LocPowerPairControlable,_W:lldpV2Xdot3LocPowerPairs,_X:lldpV2Xdot3LocPowerClass,'lldpV2Xdot3LocMaxFrameSizeTable':lldpV2Xdot3LocMaxFrameSizeTable,'lldpV2Xdot3LocMaxFrameSizeEntry':lldpV2Xdot3LocMaxFrameSizeEntry,_Y:lldpV2Xdot3LocMaxFrameSize,'lldpV2Xdot3RemoteData':lldpV2Xdot3RemoteData,'lldpV2Xdot3RemPortTable':lldpV2Xdot3RemPortTable,'lldpV2Xdot3RemPortEntry':lldpV2Xdot3RemPortEntry,_Z:lldpV2Xdot3RemPortAutoNegSupported,_a:lldpV2Xdot3RemPortAutoNegEnabled,_b:lldpV2Xdot3RemPortAutoNegAdvertisedCap,_c:lldpV2Xdot3RemPortOperMauType,'lldpV2Xdot3RemPowerTable':lldpV2Xdot3RemPowerTable,'lldpV2Xdot3RemPowerEntry':lldpV2Xdot3RemPowerEntry,_d:lldpV2Xdot3RemPowerPortClass,_e:lldpV2Xdot3RemPowerMDISupported,_f:lldpV2Xdot3RemPowerMDIEnabled,_g:lldpV2Xdot3RemPowerPairControlable,_h:lldpV2Xdot3RemPowerPairs,_i:lldpV2Xdot3RemPowerClass,'lldpV2Xdot3RemMaxFrameSizeTable':lldpV2Xdot3RemMaxFrameSizeTable,'lldpV2Xdot3RemMaxFrameSizeEntry':lldpV2Xdot3RemMaxFrameSizeEntry,_j:lldpV2Xdot3RemMaxFrameSize,'lldpV2Xdot3Conformance':lldpV2Xdot3Conformance,'lldpV2Xdot3Compliances':lldpV2Xdot3Compliances,'lldpV2Xdot3TxRxCompliance':lldpV2Xdot3TxRxCompliance,'lldpV2Xdot3TxCompliance':lldpV2Xdot3TxCompliance,'lldpV2Xdot3RxCompliance':lldpV2Xdot3RxCompliance,'lldpV2Xdot3Groups':lldpV2Xdot3Groups,_k:lldpV2Xdot3ConfigGroup,_l:lldpV2Xdot3LocSysGroup,_m:lldpV2Xdot3RemSysGroup})