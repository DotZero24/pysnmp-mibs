_J='read-only'
_I='adGenIPTVR2MulticastACLName'
_H='not-accessible'
_G='adGenIPTVR2ChannelLineupIndex'
_F='OctetString'
_E='ADTRAN-IPTVR2-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenIPTVR2,adGenIPTVR2ID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenIPTVR2','adGenIPTVR2ID')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention')
adGenIPTVR2MIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,31,26))
if mibBuilder.loadTexts:adGenIPTVR2MIB.setRevisions(('2010-06-07 00:00',))
_AdGenIPTVR2ChannelLineupTable_Object=MibTable
adGenIPTVR2ChannelLineupTable=_AdGenIPTVR2ChannelLineupTable_Object((1,3,6,1,4,1,664,5,70,31,1))
if mibBuilder.loadTexts:adGenIPTVR2ChannelLineupTable.setStatus(_A)
_AdGenIPTVR2ChannelLineupEntry_Object=MibTableRow
adGenIPTVR2ChannelLineupEntry=_AdGenIPTVR2ChannelLineupEntry_Object((1,3,6,1,4,1,664,5,70,31,1,1))
adGenIPTVR2ChannelLineupEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:adGenIPTVR2ChannelLineupEntry.setStatus(_A)
class _AdGenIPTVR2ChannelLineupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_AdGenIPTVR2ChannelLineupIndex_Type.__name__=_C
_AdGenIPTVR2ChannelLineupIndex_Object=MibTableColumn
adGenIPTVR2ChannelLineupIndex=_AdGenIPTVR2ChannelLineupIndex_Object((1,3,6,1,4,1,664,5,70,31,1,1,1),_AdGenIPTVR2ChannelLineupIndex_Type())
adGenIPTVR2ChannelLineupIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenIPTVR2ChannelLineupIndex.setStatus(_A)
class _AdGenIPTVR2ChannelLineupDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AdGenIPTVR2ChannelLineupDescription_Type.__name__=_D
_AdGenIPTVR2ChannelLineupDescription_Object=MibTableColumn
adGenIPTVR2ChannelLineupDescription=_AdGenIPTVR2ChannelLineupDescription_Object((1,3,6,1,4,1,664,5,70,31,1,1,2),_AdGenIPTVR2ChannelLineupDescription_Type())
adGenIPTVR2ChannelLineupDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIPTVR2ChannelLineupDescription.setStatus(_A)
_AdGenIPTVR2ChannelLineupStartMulticastIP_Type=IpAddress
_AdGenIPTVR2ChannelLineupStartMulticastIP_Object=MibTableColumn
adGenIPTVR2ChannelLineupStartMulticastIP=_AdGenIPTVR2ChannelLineupStartMulticastIP_Object((1,3,6,1,4,1,664,5,70,31,1,1,3),_AdGenIPTVR2ChannelLineupStartMulticastIP_Type())
adGenIPTVR2ChannelLineupStartMulticastIP.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIPTVR2ChannelLineupStartMulticastIP.setStatus(_A)
_AdGenIPTVR2ChannelLineupStopMulticastIP_Type=IpAddress
_AdGenIPTVR2ChannelLineupStopMulticastIP_Object=MibTableColumn
adGenIPTVR2ChannelLineupStopMulticastIP=_AdGenIPTVR2ChannelLineupStopMulticastIP_Object((1,3,6,1,4,1,664,5,70,31,1,1,4),_AdGenIPTVR2ChannelLineupStopMulticastIP_Type())
adGenIPTVR2ChannelLineupStopMulticastIP.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIPTVR2ChannelLineupStopMulticastIP.setStatus(_A)
_AdGenIPTVR2ChannelLineupBandwidth_Type=Integer32
_AdGenIPTVR2ChannelLineupBandwidth_Object=MibTableColumn
adGenIPTVR2ChannelLineupBandwidth=_AdGenIPTVR2ChannelLineupBandwidth_Object((1,3,6,1,4,1,664,5,70,31,1,1,5),_AdGenIPTVR2ChannelLineupBandwidth_Type())
adGenIPTVR2ChannelLineupBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIPTVR2ChannelLineupBandwidth.setStatus(_A)
class _AdGenIPTVR2ChannelLineupGuaranteed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('guaranteed',1),('nonguaranteed',2)))
_AdGenIPTVR2ChannelLineupGuaranteed_Type.__name__=_C
_AdGenIPTVR2ChannelLineupGuaranteed_Object=MibTableColumn
adGenIPTVR2ChannelLineupGuaranteed=_AdGenIPTVR2ChannelLineupGuaranteed_Object((1,3,6,1,4,1,664,5,70,31,1,1,6),_AdGenIPTVR2ChannelLineupGuaranteed_Type())
adGenIPTVR2ChannelLineupGuaranteed.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIPTVR2ChannelLineupGuaranteed.setStatus(_A)
_AdGenIPTVR2ChannelLineupLastErrorString_Type=DisplayString
_AdGenIPTVR2ChannelLineupLastErrorString_Object=MibTableColumn
adGenIPTVR2ChannelLineupLastErrorString=_AdGenIPTVR2ChannelLineupLastErrorString_Object((1,3,6,1,4,1,664,5,70,31,1,1,7),_AdGenIPTVR2ChannelLineupLastErrorString_Type())
adGenIPTVR2ChannelLineupLastErrorString.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIPTVR2ChannelLineupLastErrorString.setStatus(_A)
class _AdGenIPTVR2ChannelLineupLayer3MTU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_AdGenIPTVR2ChannelLineupLayer3MTU_Type.__name__=_C
_AdGenIPTVR2ChannelLineupLayer3MTU_Object=MibTableColumn
adGenIPTVR2ChannelLineupLayer3MTU=_AdGenIPTVR2ChannelLineupLayer3MTU_Object((1,3,6,1,4,1,664,5,70,31,1,1,8),_AdGenIPTVR2ChannelLineupLayer3MTU_Type())
adGenIPTVR2ChannelLineupLayer3MTU.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIPTVR2ChannelLineupLayer3MTU.setStatus(_A)
_AdGenIPTVR2ChannelLineupRowStatus_Type=RowStatus
_AdGenIPTVR2ChannelLineupRowStatus_Object=MibTableColumn
adGenIPTVR2ChannelLineupRowStatus=_AdGenIPTVR2ChannelLineupRowStatus_Object((1,3,6,1,4,1,664,5,70,31,1,1,9),_AdGenIPTVR2ChannelLineupRowStatus_Type())
adGenIPTVR2ChannelLineupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIPTVR2ChannelLineupRowStatus.setStatus(_A)
_AdGenIPTVR2MulticastACLTable_Object=MibTable
adGenIPTVR2MulticastACLTable=_AdGenIPTVR2MulticastACLTable_Object((1,3,6,1,4,1,664,5,70,31,2))
if mibBuilder.loadTexts:adGenIPTVR2MulticastACLTable.setStatus(_A)
_AdGenIPTVR2MulticastACLEntry_Object=MibTableRow
adGenIPTVR2MulticastACLEntry=_AdGenIPTVR2MulticastACLEntry_Object((1,3,6,1,4,1,664,5,70,31,2,1))
adGenIPTVR2MulticastACLEntry.setIndexNames((1,_E,_I))
if mibBuilder.loadTexts:adGenIPTVR2MulticastACLEntry.setStatus(_A)
class _AdGenIPTVR2MulticastACLName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AdGenIPTVR2MulticastACLName_Type.__name__=_D
_AdGenIPTVR2MulticastACLName_Object=MibTableColumn
adGenIPTVR2MulticastACLName=_AdGenIPTVR2MulticastACLName_Object((1,3,6,1,4,1,664,5,70,31,2,1,1),_AdGenIPTVR2MulticastACLName_Type())
adGenIPTVR2MulticastACLName.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenIPTVR2MulticastACLName.setStatus(_A)
_AdGenIPTVR2MulticastACLLastErrorString_Type=DisplayString
_AdGenIPTVR2MulticastACLLastErrorString_Object=MibTableColumn
adGenIPTVR2MulticastACLLastErrorString=_AdGenIPTVR2MulticastACLLastErrorString_Object((1,3,6,1,4,1,664,5,70,31,2,1,2),_AdGenIPTVR2MulticastACLLastErrorString_Type())
adGenIPTVR2MulticastACLLastErrorString.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIPTVR2MulticastACLLastErrorString.setStatus(_A)
class _AdGenIPTVR2MulticastACLList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AdGenIPTVR2MulticastACLList_Type.__name__=_F
_AdGenIPTVR2MulticastACLList_Object=MibTableColumn
adGenIPTVR2MulticastACLList=_AdGenIPTVR2MulticastACLList_Object((1,3,6,1,4,1,664,5,70,31,2,1,3),_AdGenIPTVR2MulticastACLList_Type())
adGenIPTVR2MulticastACLList.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIPTVR2MulticastACLList.setStatus(_A)
_AdGenIPTVR2MulticastACLRowStatus_Type=RowStatus
_AdGenIPTVR2MulticastACLRowStatus_Object=MibTableColumn
adGenIPTVR2MulticastACLRowStatus=_AdGenIPTVR2MulticastACLRowStatus_Object((1,3,6,1,4,1,664,5,70,31,2,1,4),_AdGenIPTVR2MulticastACLRowStatus_Type())
adGenIPTVR2MulticastACLRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIPTVR2MulticastACLRowStatus.setStatus(_A)
_AdGenIPTVR2Scalars_ObjectIdentity=ObjectIdentity
adGenIPTVR2Scalars=_AdGenIPTVR2Scalars_ObjectIdentity((1,3,6,1,4,1,664,5,70,31,3))
_AdGenIPTVR2ChannelLineupLastCreateError_Type=DisplayString
_AdGenIPTVR2ChannelLineupLastCreateError_Object=MibScalar
adGenIPTVR2ChannelLineupLastCreateError=_AdGenIPTVR2ChannelLineupLastCreateError_Object((1,3,6,1,4,1,664,5,70,31,3,1),_AdGenIPTVR2ChannelLineupLastCreateError_Type())
adGenIPTVR2ChannelLineupLastCreateError.setMaxAccess(_J)
if mibBuilder.loadTexts:adGenIPTVR2ChannelLineupLastCreateError.setStatus(_A)
_AdGenIPTVR2MulticastACLLastCreateError_Type=DisplayString
_AdGenIPTVR2MulticastACLLastCreateError_Object=MibScalar
adGenIPTVR2MulticastACLLastCreateError=_AdGenIPTVR2MulticastACLLastCreateError_Object((1,3,6,1,4,1,664,5,70,31,3,2),_AdGenIPTVR2MulticastACLLastCreateError_Type())
adGenIPTVR2MulticastACLLastCreateError.setMaxAccess(_J)
if mibBuilder.loadTexts:adGenIPTVR2MulticastACLLastCreateError.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'adGenIPTVR2ChannelLineupTable':adGenIPTVR2ChannelLineupTable,'adGenIPTVR2ChannelLineupEntry':adGenIPTVR2ChannelLineupEntry,_G:adGenIPTVR2ChannelLineupIndex,'adGenIPTVR2ChannelLineupDescription':adGenIPTVR2ChannelLineupDescription,'adGenIPTVR2ChannelLineupStartMulticastIP':adGenIPTVR2ChannelLineupStartMulticastIP,'adGenIPTVR2ChannelLineupStopMulticastIP':adGenIPTVR2ChannelLineupStopMulticastIP,'adGenIPTVR2ChannelLineupBandwidth':adGenIPTVR2ChannelLineupBandwidth,'adGenIPTVR2ChannelLineupGuaranteed':adGenIPTVR2ChannelLineupGuaranteed,'adGenIPTVR2ChannelLineupLastErrorString':adGenIPTVR2ChannelLineupLastErrorString,'adGenIPTVR2ChannelLineupLayer3MTU':adGenIPTVR2ChannelLineupLayer3MTU,'adGenIPTVR2ChannelLineupRowStatus':adGenIPTVR2ChannelLineupRowStatus,'adGenIPTVR2MulticastACLTable':adGenIPTVR2MulticastACLTable,'adGenIPTVR2MulticastACLEntry':adGenIPTVR2MulticastACLEntry,_I:adGenIPTVR2MulticastACLName,'adGenIPTVR2MulticastACLLastErrorString':adGenIPTVR2MulticastACLLastErrorString,'adGenIPTVR2MulticastACLList':adGenIPTVR2MulticastACLList,'adGenIPTVR2MulticastACLRowStatus':adGenIPTVR2MulticastACLRowStatus,'adGenIPTVR2Scalars':adGenIPTVR2Scalars,'adGenIPTVR2ChannelLineupLastCreateError':adGenIPTVR2ChannelLineupLastCreateError,'adGenIPTVR2MulticastACLLastCreateError':adGenIPTVR2MulticastACLLastCreateError,'adGenIPTVR2MIB':adGenIPTVR2MIB})