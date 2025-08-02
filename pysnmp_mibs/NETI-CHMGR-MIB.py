_e='chmgrChanOutgoingIfPort'
_d='chmgrChanOutgoingIfBoard'
_c='chmgrChanChannelId'
_b='chmgrChanSourceMacAddress'
_a='chmgrTChanIndex'
_Z='reestablish'
_Y='notApplicable'
_X='dormant'
_W='chmgrSourceRouteHopIndex'
_V='chmgrODescrChanSourceRouteIndex'
_U='DtmNode'
_T='deprecated'
_S='chmgrSourceRouteIndex'
_R='chmgrODescrChanIndex'
_Q='TruthValue'
_P='Bits'
_O='chmgrODescrIndex'
_N='chmgrTConnIndex'
_M='chmgrOConnIndex'
_L='chmgrODescrDestIndex'
_K='Gauge32'
_J='down'
_I='up'
_H='Integer32'
_G='not-accessible'
_F='Unsigned32'
_E='read-create'
_D='read-write'
_C='NETI-CHMGR-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netiExperimentalGeneric,=mibBuilder.importSymbols('NETI-COMMON-MIB','netiExperimentalGeneric')
DtmAddress,=mibBuilder.importSymbols('NETI-DTM-MIB','DtmAddress')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_P,'Counter32','Counter64',_K,_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowPointer','RowStatus','TextualConvention','TimeStamp',_Q)
netiChmgrMIB=ModuleIdentity((1,3,6,1,4,1,2928,6,2,14))
if mibBuilder.loadTexts:netiChmgrMIB.setRevisions(('2015-01-08 15:00','2014-05-05 12:00','2014-02-06 15:00','2013-09-02 16:00','2012-03-19 09:00','2012-01-26 15:00','2010-04-06 08:00','2009-09-25 11:00','2008-12-12 14:00','2008-01-28 14:00','2008-01-03 16:00','2007-06-29 12:00','2006-09-20 08:00','2006-04-20 09:00','2005-09-27 00:00','2004-11-18 00:00','2003-04-24 00:00'))
class Dst(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,5,8,12,13,14,15,16,18,19,20,21,22,23,24,25,26)));namedValues=NamedValues(*(('ctrl',0),('dleCrtlAndData',1),('pdh',4),('dleInterServer',5),('ets',8),('ping',12),('e1',13),('ds1',14),('sdi',15),('dvb',16),('sdh',18),('ttcp',19),('aesebu',20),('j2kSdSdi',21),('j2kHdSdi',22),('j2k3gSdi',23),('j2kHdSdi2',24),('j2k3gSdi2',25),('j2kSdSdi2',26)))
class Dsti(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32769))
class ChannelId(TextualConvention,Unsigned32):status=_A;displayHint='x'
class DcapType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dcap0',1),('dcap1',2)))
class DtmNode(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
class DcpVersion(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('dcp2',2),('dcp3',3)))
_ChmgrObjects_ObjectIdentity=ObjectIdentity
chmgrObjects=_ChmgrObjects_ObjectIdentity((1,3,6,1,4,1,2928,6,2,14,1))
_ChmgrODescriptionGroup_ObjectIdentity=ObjectIdentity
chmgrODescriptionGroup=_ChmgrODescriptionGroup_ObjectIdentity((1,3,6,1,4,1,2928,6,2,14,1,1))
_ChmgrODescriptionTimeStamp_Type=TimeStamp
_ChmgrODescriptionTimeStamp_Object=MibScalar
chmgrODescriptionTimeStamp=_ChmgrODescriptionTimeStamp_Object((1,3,6,1,4,1,2928,6,2,14,1,1,1),_ChmgrODescriptionTimeStamp_Type())
chmgrODescriptionTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrODescriptionTimeStamp.setStatus(_A)
_ChmgrODescriptionTable_Object=MibTable
chmgrODescriptionTable=_ChmgrODescriptionTable_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2))
if mibBuilder.loadTexts:chmgrODescriptionTable.setStatus(_A)
_ChmgrODescriptionEntry_Object=MibTableRow
chmgrODescriptionEntry=_ChmgrODescriptionEntry_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2,1))
chmgrODescriptionEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:chmgrODescriptionEntry.setStatus(_A)
_ChmgrODescrIndex_Type=Unsigned32
_ChmgrODescrIndex_Object=MibTableColumn
chmgrODescrIndex=_ChmgrODescrIndex_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2,1,1),_ChmgrODescrIndex_Type())
chmgrODescrIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:chmgrODescrIndex.setStatus(_A)
class _ChmgrODescrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ets',1),('its',2),('dle',3)))
_ChmgrODescrType_Type.__name__=_H
_ChmgrODescrType_Object=MibTableColumn
chmgrODescrType=_ChmgrODescrType_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2,1,2),_ChmgrODescrType_Type())
chmgrODescrType.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrODescrType.setStatus(_A)
class _ChmgrODescrCapabilities_Type(Bits):namedValues=NamedValues(*(('allowCapacityInterval',0),('destination',1),('allowDynamicCapacity',2),('isMulticast',3),('allowEstablish',4),('allowProtection',5),('allowReestablish',6),('allowScheduling',7),('allowSourceRoute',8),('requireCapacity',9),('allowAlternative',10),('allowZeroCapacity',11)))
_ChmgrODescrCapabilities_Type.__name__=_P
_ChmgrODescrCapabilities_Object=MibTableColumn
chmgrODescrCapabilities=_ChmgrODescrCapabilities_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2,1,3),_ChmgrODescrCapabilities_Type())
chmgrODescrCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrODescrCapabilities.setStatus(_A)
_ChmgrODescrCustomerId_Type=Unsigned32
_ChmgrODescrCustomerId_Object=MibTableColumn
chmgrODescrCustomerId=_ChmgrODescrCustomerId_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2,1,4),_ChmgrODescrCustomerId_Type())
chmgrODescrCustomerId.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrODescrCustomerId.setStatus(_A)
_ChmgrODescrServiceReference_Type=RowPointer
_ChmgrODescrServiceReference_Object=MibTableColumn
chmgrODescrServiceReference=_ChmgrODescrServiceReference_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2,1,5),_ChmgrODescrServiceReference_Type())
chmgrODescrServiceReference.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrODescrServiceReference.setStatus(_A)
_ChmgrODescrAcceptableBps_Type=Gauge32
_ChmgrODescrAcceptableBps_Object=MibTableColumn
chmgrODescrAcceptableBps=_ChmgrODescrAcceptableBps_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2,1,6),_ChmgrODescrAcceptableBps_Type())
chmgrODescrAcceptableBps.setMaxAccess(_D)
if mibBuilder.loadTexts:chmgrODescrAcceptableBps.setStatus(_A)
_ChmgrODescrAcceptableSlots_Type=Gauge32
_ChmgrODescrAcceptableSlots_Object=MibTableColumn
chmgrODescrAcceptableSlots=_ChmgrODescrAcceptableSlots_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2,1,7),_ChmgrODescrAcceptableSlots_Type())
chmgrODescrAcceptableSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrODescrAcceptableSlots.setStatus(_A)
_ChmgrODescrRequestedBps_Type=Gauge32
_ChmgrODescrRequestedBps_Object=MibTableColumn
chmgrODescrRequestedBps=_ChmgrODescrRequestedBps_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2,1,8),_ChmgrODescrRequestedBps_Type())
chmgrODescrRequestedBps.setMaxAccess(_D)
if mibBuilder.loadTexts:chmgrODescrRequestedBps.setStatus(_A)
_ChmgrODescrRequestedSlots_Type=Gauge32
_ChmgrODescrRequestedSlots_Object=MibTableColumn
chmgrODescrRequestedSlots=_ChmgrODescrRequestedSlots_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2,1,9),_ChmgrODescrRequestedSlots_Type())
chmgrODescrRequestedSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrODescrRequestedSlots.setStatus(_A)
class _ChmgrODescrReestablishMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('exponential',1))
_ChmgrODescrReestablishMethod_Type.__name__=_H
_ChmgrODescrReestablishMethod_Object=MibTableColumn
chmgrODescrReestablishMethod=_ChmgrODescrReestablishMethod_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2,1,10),_ChmgrODescrReestablishMethod_Type())
chmgrODescrReestablishMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:chmgrODescrReestablishMethod.setStatus(_A)
class _ChmgrODescrMinInterval_Type(Gauge32):defaultValue=500;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_ChmgrODescrMinInterval_Type.__name__=_K
_ChmgrODescrMinInterval_Object=MibTableColumn
chmgrODescrMinInterval=_ChmgrODescrMinInterval_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2,1,11),_ChmgrODescrMinInterval_Type())
chmgrODescrMinInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:chmgrODescrMinInterval.setStatus(_A)
class _ChmgrODescrMaxInterval_Type(Gauge32):defaultValue=10000;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_ChmgrODescrMaxInterval_Type.__name__=_K
_ChmgrODescrMaxInterval_Object=MibTableColumn
chmgrODescrMaxInterval=_ChmgrODescrMaxInterval_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2,1,12),_ChmgrODescrMaxInterval_Type())
chmgrODescrMaxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:chmgrODescrMaxInterval.setStatus(_A)
class _ChmgrODescrEstablish_Type(TruthValue):defaultValue=1
_ChmgrODescrEstablish_Type.__name__=_Q
_ChmgrODescrEstablish_Object=MibTableColumn
chmgrODescrEstablish=_ChmgrODescrEstablish_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2,1,13),_ChmgrODescrEstablish_Type())
chmgrODescrEstablish.setMaxAccess(_D)
if mibBuilder.loadTexts:chmgrODescrEstablish.setStatus(_A)
class _ChmgrODescrNextDestTableIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_ChmgrODescrNextDestTableIndex_Type.__name__=_F
_ChmgrODescrNextDestTableIndex_Object=MibTableColumn
chmgrODescrNextDestTableIndex=_ChmgrODescrNextDestTableIndex_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2,1,14),_ChmgrODescrNextDestTableIndex_Type())
chmgrODescrNextDestTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrODescrNextDestTableIndex.setStatus(_A)
class _ChmgrODescrPrecedence_Type(TruthValue):defaultValue=2
_ChmgrODescrPrecedence_Type.__name__=_Q
_ChmgrODescrPrecedence_Object=MibTableColumn
chmgrODescrPrecedence=_ChmgrODescrPrecedence_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2,1,15),_ChmgrODescrPrecedence_Type())
chmgrODescrPrecedence.setMaxAccess(_D)
if mibBuilder.loadTexts:chmgrODescrPrecedence.setStatus(_A)
class _ChmgrODescrSuppressAlarms_Type(Bits):namedValues=NamedValues(('route',0))
_ChmgrODescrSuppressAlarms_Type.__name__=_P
_ChmgrODescrSuppressAlarms_Object=MibTableColumn
chmgrODescrSuppressAlarms=_ChmgrODescrSuppressAlarms_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2,1,16),_ChmgrODescrSuppressAlarms_Type())
chmgrODescrSuppressAlarms.setMaxAccess(_D)
if mibBuilder.loadTexts:chmgrODescrSuppressAlarms.setStatus(_A)
_ChmgrODescrAcceptableMbps_Type=Gauge32
_ChmgrODescrAcceptableMbps_Object=MibTableColumn
chmgrODescrAcceptableMbps=_ChmgrODescrAcceptableMbps_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2,1,17),_ChmgrODescrAcceptableMbps_Type())
chmgrODescrAcceptableMbps.setMaxAccess(_D)
if mibBuilder.loadTexts:chmgrODescrAcceptableMbps.setStatus(_A)
_ChmgrODescrRequestedMbps_Type=Gauge32
_ChmgrODescrRequestedMbps_Object=MibTableColumn
chmgrODescrRequestedMbps=_ChmgrODescrRequestedMbps_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2,1,18),_ChmgrODescrRequestedMbps_Type())
chmgrODescrRequestedMbps.setMaxAccess(_D)
if mibBuilder.loadTexts:chmgrODescrRequestedMbps.setStatus(_A)
_ChmgrODescrRequestedDcpVersion_Type=DcpVersion
_ChmgrODescrRequestedDcpVersion_Object=MibTableColumn
chmgrODescrRequestedDcpVersion=_ChmgrODescrRequestedDcpVersion_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2,1,19),_ChmgrODescrRequestedDcpVersion_Type())
chmgrODescrRequestedDcpVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:chmgrODescrRequestedDcpVersion.setStatus(_A)
_ChmgrODescrOneHopSpareCapUtilization_Type=TruthValue
_ChmgrODescrOneHopSpareCapUtilization_Object=MibTableColumn
chmgrODescrOneHopSpareCapUtilization=_ChmgrODescrOneHopSpareCapUtilization_Object((1,3,6,1,4,1,2928,6,2,14,1,1,2,1,20),_ChmgrODescrOneHopSpareCapUtilization_Type())
chmgrODescrOneHopSpareCapUtilization.setMaxAccess(_D)
if mibBuilder.loadTexts:chmgrODescrOneHopSpareCapUtilization.setStatus(_A)
_ChmgrODescrDestinationTable_Object=MibTable
chmgrODescrDestinationTable=_ChmgrODescrDestinationTable_Object((1,3,6,1,4,1,2928,6,2,14,1,1,3))
if mibBuilder.loadTexts:chmgrODescrDestinationTable.setStatus(_A)
_ChmgrODescrDestinationEntry_Object=MibTableRow
chmgrODescrDestinationEntry=_ChmgrODescrDestinationEntry_Object((1,3,6,1,4,1,2928,6,2,14,1,1,3,1))
chmgrODescrDestinationEntry.setIndexNames((0,_C,_O),(0,_C,_L))
if mibBuilder.loadTexts:chmgrODescrDestinationEntry.setStatus(_A)
_ChmgrODescrDestIndex_Type=Unsigned32
_ChmgrODescrDestIndex_Object=MibTableColumn
chmgrODescrDestIndex=_ChmgrODescrDestIndex_Object((1,3,6,1,4,1,2928,6,2,14,1,1,3,1,1),_ChmgrODescrDestIndex_Type())
chmgrODescrDestIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:chmgrODescrDestIndex.setStatus(_A)
class _ChmgrODescrDestAddress_Type(DtmNode):defaultHexValue=''
_ChmgrODescrDestAddress_Type.__name__=_U
_ChmgrODescrDestAddress_Object=MibTableColumn
chmgrODescrDestAddress=_ChmgrODescrDestAddress_Object((1,3,6,1,4,1,2928,6,2,14,1,1,3,1,2),_ChmgrODescrDestAddress_Type())
chmgrODescrDestAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:chmgrODescrDestAddress.setStatus(_A)
class _ChmgrODescrDestDsti_Type(Dsti):defaultValue=0
_ChmgrODescrDestDsti_Type.__name__='Dsti'
_ChmgrODescrDestDsti_Object=MibTableColumn
chmgrODescrDestDsti=_ChmgrODescrDestDsti_Object((1,3,6,1,4,1,2928,6,2,14,1,1,3,1,3),_ChmgrODescrDestDsti_Type())
chmgrODescrDestDsti.setMaxAccess(_E)
if mibBuilder.loadTexts:chmgrODescrDestDsti.setStatus(_A)
_ChmgrODescrDestRowStatus_Type=RowStatus
_ChmgrODescrDestRowStatus_Object=MibTableColumn
chmgrODescrDestRowStatus=_ChmgrODescrDestRowStatus_Object((1,3,6,1,4,1,2928,6,2,14,1,1,3,1,4),_ChmgrODescrDestRowStatus_Type())
chmgrODescrDestRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:chmgrODescrDestRowStatus.setStatus(_A)
class _ChmgrODescrDestAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_ChmgrODescrDestAdminStatus_Type.__name__=_H
_ChmgrODescrDestAdminStatus_Object=MibTableColumn
chmgrODescrDestAdminStatus=_ChmgrODescrDestAdminStatus_Object((1,3,6,1,4,1,2928,6,2,14,1,1,3,1,5),_ChmgrODescrDestAdminStatus_Type())
chmgrODescrDestAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:chmgrODescrDestAdminStatus.setStatus(_A)
_ChmgrODescrChannelTable_Object=MibTable
chmgrODescrChannelTable=_ChmgrODescrChannelTable_Object((1,3,6,1,4,1,2928,6,2,14,1,1,4))
if mibBuilder.loadTexts:chmgrODescrChannelTable.setStatus(_A)
_ChmgrODescrChannelEntry_Object=MibTableRow
chmgrODescrChannelEntry=_ChmgrODescrChannelEntry_Object((1,3,6,1,4,1,2928,6,2,14,1,1,4,1))
chmgrODescrChannelEntry.setIndexNames((0,_C,_O),(0,_C,_L),(0,_C,_R),(0,_C,_V))
if mibBuilder.loadTexts:chmgrODescrChannelEntry.setStatus(_A)
class _ChmgrODescrChanIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_ChmgrODescrChanIndex_Type.__name__=_F
_ChmgrODescrChanIndex_Object=MibTableColumn
chmgrODescrChanIndex=_ChmgrODescrChanIndex_Object((1,3,6,1,4,1,2928,6,2,14,1,1,4,1,1),_ChmgrODescrChanIndex_Type())
chmgrODescrChanIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:chmgrODescrChanIndex.setStatus(_A)
_ChmgrODescrChanSourceRouteIndex_Type=Unsigned32
_ChmgrODescrChanSourceRouteIndex_Object=MibTableColumn
chmgrODescrChanSourceRouteIndex=_ChmgrODescrChanSourceRouteIndex_Object((1,3,6,1,4,1,2928,6,2,14,1,1,4,1,2),_ChmgrODescrChanSourceRouteIndex_Type())
chmgrODescrChanSourceRouteIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:chmgrODescrChanSourceRouteIndex.setStatus(_A)
_ChmgrODescrChanSourceRoute_Type=Unsigned32
_ChmgrODescrChanSourceRoute_Object=MibTableColumn
chmgrODescrChanSourceRoute=_ChmgrODescrChanSourceRoute_Object((1,3,6,1,4,1,2928,6,2,14,1,1,4,1,3),_ChmgrODescrChanSourceRoute_Type())
chmgrODescrChanSourceRoute.setMaxAccess(_E)
if mibBuilder.loadTexts:chmgrODescrChanSourceRoute.setStatus(_A)
_ChmgrODescrChanRowStatus_Type=RowStatus
_ChmgrODescrChanRowStatus_Object=MibTableColumn
chmgrODescrChanRowStatus=_ChmgrODescrChanRowStatus_Object((1,3,6,1,4,1,2928,6,2,14,1,1,4,1,4),_ChmgrODescrChanRowStatus_Type())
chmgrODescrChanRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:chmgrODescrChanRowStatus.setStatus(_A)
_ChmgrTDescriptionGroup_ObjectIdentity=ObjectIdentity
chmgrTDescriptionGroup=_ChmgrTDescriptionGroup_ObjectIdentity((1,3,6,1,4,1,2928,6,2,14,1,2))
_ChmgrSourceRouteGroup_ObjectIdentity=ObjectIdentity
chmgrSourceRouteGroup=_ChmgrSourceRouteGroup_ObjectIdentity((1,3,6,1,4,1,2928,6,2,14,1,3))
_ChmgrSourceRouteTimeStamp_Type=TimeStamp
_ChmgrSourceRouteTimeStamp_Object=MibScalar
chmgrSourceRouteTimeStamp=_ChmgrSourceRouteTimeStamp_Object((1,3,6,1,4,1,2928,6,2,14,1,3,1),_ChmgrSourceRouteTimeStamp_Type())
chmgrSourceRouteTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrSourceRouteTimeStamp.setStatus(_A)
_ChmgrSourceRouteTable_Object=MibTable
chmgrSourceRouteTable=_ChmgrSourceRouteTable_Object((1,3,6,1,4,1,2928,6,2,14,1,3,2))
if mibBuilder.loadTexts:chmgrSourceRouteTable.setStatus(_A)
_ChmgrSourceRouteEntry_Object=MibTableRow
chmgrSourceRouteEntry=_ChmgrSourceRouteEntry_Object((1,3,6,1,4,1,2928,6,2,14,1,3,2,1))
chmgrSourceRouteEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:chmgrSourceRouteEntry.setStatus(_A)
_ChmgrSourceRouteIndex_Type=Unsigned32
_ChmgrSourceRouteIndex_Object=MibTableColumn
chmgrSourceRouteIndex=_ChmgrSourceRouteIndex_Object((1,3,6,1,4,1,2928,6,2,14,1,3,2,1,1),_ChmgrSourceRouteIndex_Type())
chmgrSourceRouteIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:chmgrSourceRouteIndex.setStatus(_A)
_ChmgrSourceRouteName_Type=SnmpAdminString
_ChmgrSourceRouteName_Object=MibTableColumn
chmgrSourceRouteName=_ChmgrSourceRouteName_Object((1,3,6,1,4,1,2928,6,2,14,1,3,2,1,2),_ChmgrSourceRouteName_Type())
chmgrSourceRouteName.setMaxAccess(_D)
if mibBuilder.loadTexts:chmgrSourceRouteName.setStatus(_A)
class _ChmgrSourceRouteTypeOfRoute_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('strict',1),('loose',2)))
_ChmgrSourceRouteTypeOfRoute_Type.__name__=_H
_ChmgrSourceRouteTypeOfRoute_Object=MibTableColumn
chmgrSourceRouteTypeOfRoute=_ChmgrSourceRouteTypeOfRoute_Object((1,3,6,1,4,1,2928,6,2,14,1,3,2,1,3),_ChmgrSourceRouteTypeOfRoute_Type())
chmgrSourceRouteTypeOfRoute.setMaxAccess(_E)
if mibBuilder.loadTexts:chmgrSourceRouteTypeOfRoute.setStatus(_A)
class _ChmgrSourceRouteFirstIfBoard_Type(Unsigned32):defaultValue=0
_ChmgrSourceRouteFirstIfBoard_Type.__name__=_F
_ChmgrSourceRouteFirstIfBoard_Object=MibTableColumn
chmgrSourceRouteFirstIfBoard=_ChmgrSourceRouteFirstIfBoard_Object((1,3,6,1,4,1,2928,6,2,14,1,3,2,1,4),_ChmgrSourceRouteFirstIfBoard_Type())
chmgrSourceRouteFirstIfBoard.setMaxAccess(_E)
if mibBuilder.loadTexts:chmgrSourceRouteFirstIfBoard.setStatus(_A)
class _ChmgrSourceRouteFirstIfPort_Type(Unsigned32):defaultValue=0
_ChmgrSourceRouteFirstIfPort_Type.__name__=_F
_ChmgrSourceRouteFirstIfPort_Object=MibTableColumn
chmgrSourceRouteFirstIfPort=_ChmgrSourceRouteFirstIfPort_Object((1,3,6,1,4,1,2928,6,2,14,1,3,2,1,5),_ChmgrSourceRouteFirstIfPort_Type())
chmgrSourceRouteFirstIfPort.setMaxAccess(_E)
if mibBuilder.loadTexts:chmgrSourceRouteFirstIfPort.setStatus(_A)
_ChmgrSourceRouteRowStatus_Type=RowStatus
_ChmgrSourceRouteRowStatus_Object=MibTableColumn
chmgrSourceRouteRowStatus=_ChmgrSourceRouteRowStatus_Object((1,3,6,1,4,1,2928,6,2,14,1,3,2,1,6),_ChmgrSourceRouteRowStatus_Type())
chmgrSourceRouteRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:chmgrSourceRouteRowStatus.setStatus(_A)
_ChmgrSourceRouteHopTable_Object=MibTable
chmgrSourceRouteHopTable=_ChmgrSourceRouteHopTable_Object((1,3,6,1,4,1,2928,6,2,14,1,3,3))
if mibBuilder.loadTexts:chmgrSourceRouteHopTable.setStatus(_A)
_ChmgrSourceRouteHopEntry_Object=MibTableRow
chmgrSourceRouteHopEntry=_ChmgrSourceRouteHopEntry_Object((1,3,6,1,4,1,2928,6,2,14,1,3,3,1))
chmgrSourceRouteHopEntry.setIndexNames((0,_C,_S),(0,_C,_W))
if mibBuilder.loadTexts:chmgrSourceRouteHopEntry.setStatus(_A)
_ChmgrSourceRouteHopIndex_Type=Unsigned32
_ChmgrSourceRouteHopIndex_Object=MibTableColumn
chmgrSourceRouteHopIndex=_ChmgrSourceRouteHopIndex_Object((1,3,6,1,4,1,2928,6,2,14,1,3,3,1,1),_ChmgrSourceRouteHopIndex_Type())
chmgrSourceRouteHopIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:chmgrSourceRouteHopIndex.setStatus(_A)
_ChmgrSourceRouteHopAddress_Type=DtmNode
_ChmgrSourceRouteHopAddress_Object=MibTableColumn
chmgrSourceRouteHopAddress=_ChmgrSourceRouteHopAddress_Object((1,3,6,1,4,1,2928,6,2,14,1,3,3,1,2),_ChmgrSourceRouteHopAddress_Type())
chmgrSourceRouteHopAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:chmgrSourceRouteHopAddress.setStatus(_A)
class _ChmgrSourceRouteHopNextIfBoard_Type(Unsigned32):defaultValue=0
_ChmgrSourceRouteHopNextIfBoard_Type.__name__=_F
_ChmgrSourceRouteHopNextIfBoard_Object=MibTableColumn
chmgrSourceRouteHopNextIfBoard=_ChmgrSourceRouteHopNextIfBoard_Object((1,3,6,1,4,1,2928,6,2,14,1,3,3,1,3),_ChmgrSourceRouteHopNextIfBoard_Type())
chmgrSourceRouteHopNextIfBoard.setMaxAccess(_E)
if mibBuilder.loadTexts:chmgrSourceRouteHopNextIfBoard.setStatus(_A)
class _ChmgrSourceRouteHopNextIfPort_Type(Unsigned32):defaultValue=0
_ChmgrSourceRouteHopNextIfPort_Type.__name__=_F
_ChmgrSourceRouteHopNextIfPort_Object=MibTableColumn
chmgrSourceRouteHopNextIfPort=_ChmgrSourceRouteHopNextIfPort_Object((1,3,6,1,4,1,2928,6,2,14,1,3,3,1,4),_ChmgrSourceRouteHopNextIfPort_Type())
chmgrSourceRouteHopNextIfPort.setMaxAccess(_E)
if mibBuilder.loadTexts:chmgrSourceRouteHopNextIfPort.setStatus(_A)
_ChmgrSourceRouteHopRowStatus_Type=RowStatus
_ChmgrSourceRouteHopRowStatus_Object=MibTableColumn
chmgrSourceRouteHopRowStatus=_ChmgrSourceRouteHopRowStatus_Object((1,3,6,1,4,1,2928,6,2,14,1,3,3,1,5),_ChmgrSourceRouteHopRowStatus_Type())
chmgrSourceRouteHopRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:chmgrSourceRouteHopRowStatus.setStatus(_A)
_ChmgrOConnectionGroup_ObjectIdentity=ObjectIdentity
chmgrOConnectionGroup=_ChmgrOConnectionGroup_ObjectIdentity((1,3,6,1,4,1,2928,6,2,14,1,4))
_ChmgrOConnectionTimeStamp_Type=TimeStamp
_ChmgrOConnectionTimeStamp_Object=MibScalar
chmgrOConnectionTimeStamp=_ChmgrOConnectionTimeStamp_Object((1,3,6,1,4,1,2928,6,2,14,1,4,1),_ChmgrOConnectionTimeStamp_Type())
chmgrOConnectionTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOConnectionTimeStamp.setStatus(_A)
_ChmgrOConnectionTable_Object=MibTable
chmgrOConnectionTable=_ChmgrOConnectionTable_Object((1,3,6,1,4,1,2928,6,2,14,1,4,2))
if mibBuilder.loadTexts:chmgrOConnectionTable.setStatus(_A)
_ChmgrOConnectionEntry_Object=MibTableRow
chmgrOConnectionEntry=_ChmgrOConnectionEntry_Object((1,3,6,1,4,1,2928,6,2,14,1,4,2,1))
chmgrOConnectionEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:chmgrOConnectionEntry.setStatus(_A)
_ChmgrOConnIndex_Type=Unsigned32
_ChmgrOConnIndex_Object=MibTableColumn
chmgrOConnIndex=_ChmgrOConnIndex_Object((1,3,6,1,4,1,2928,6,2,14,1,4,2,1,1),_ChmgrOConnIndex_Type())
chmgrOConnIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:chmgrOConnIndex.setStatus(_A)
_ChmgrOConnCustomerId_Type=Unsigned32
_ChmgrOConnCustomerId_Object=MibTableColumn
chmgrOConnCustomerId=_ChmgrOConnCustomerId_Object((1,3,6,1,4,1,2928,6,2,14,1,4,2,1,2),_ChmgrOConnCustomerId_Type())
chmgrOConnCustomerId.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOConnCustomerId.setStatus(_A)
class _ChmgrOConnODescrIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_ChmgrOConnODescrIndex_Type.__name__=_F
_ChmgrOConnODescrIndex_Object=MibTableColumn
chmgrOConnODescrIndex=_ChmgrOConnODescrIndex_Object((1,3,6,1,4,1,2928,6,2,14,1,4,2,1,3),_ChmgrOConnODescrIndex_Type())
chmgrOConnODescrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOConnODescrIndex.setStatus(_A)
_ChmgrOConnServiceReference_Type=RowPointer
_ChmgrOConnServiceReference_Object=MibTableColumn
chmgrOConnServiceReference=_ChmgrOConnServiceReference_Object((1,3,6,1,4,1,2928,6,2,14,1,4,2,1,4),_ChmgrOConnServiceReference_Type())
chmgrOConnServiceReference.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOConnServiceReference.setStatus(_A)
class _ChmgrOConnAllocatedSlots_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8389))
_ChmgrOConnAllocatedSlots_Type.__name__=_K
_ChmgrOConnAllocatedSlots_Object=MibTableColumn
chmgrOConnAllocatedSlots=_ChmgrOConnAllocatedSlots_Object((1,3,6,1,4,1,2928,6,2,14,1,4,2,1,5),_ChmgrOConnAllocatedSlots_Type())
chmgrOConnAllocatedSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOConnAllocatedSlots.setStatus(_A)
_ChmgrOConnAllocatedSlotsChanged_Type=TimeStamp
_ChmgrOConnAllocatedSlotsChanged_Object=MibTableColumn
chmgrOConnAllocatedSlotsChanged=_ChmgrOConnAllocatedSlotsChanged_Object((1,3,6,1,4,1,2928,6,2,14,1,4,2,1,6),_ChmgrOConnAllocatedSlotsChanged_Type())
chmgrOConnAllocatedSlotsChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOConnAllocatedSlotsChanged.setStatus(_A)
_ChmgrOConnDcapType_Type=DcapType
_ChmgrOConnDcapType_Object=MibTableColumn
chmgrOConnDcapType=_ChmgrOConnDcapType_Object((1,3,6,1,4,1,2928,6,2,14,1,4,2,1,7),_ChmgrOConnDcapType_Type())
chmgrOConnDcapType.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOConnDcapType.setStatus(_A)
_ChmgrOConnDst_Type=Dst
_ChmgrOConnDst_Object=MibTableColumn
chmgrOConnDst=_ChmgrOConnDst_Object((1,3,6,1,4,1,2928,6,2,14,1,4,2,1,8),_ChmgrOConnDst_Type())
chmgrOConnDst.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOConnDst.setStatus(_A)
_ChmgrOConnSourceAddress_Type=DtmNode
_ChmgrOConnSourceAddress_Object=MibTableColumn
chmgrOConnSourceAddress=_ChmgrOConnSourceAddress_Object((1,3,6,1,4,1,2928,6,2,14,1,4,2,1,9),_ChmgrOConnSourceAddress_Type())
chmgrOConnSourceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOConnSourceAddress.setStatus(_A)
_ChmgrOConnSourceDsti_Type=Dsti
_ChmgrOConnSourceDsti_Object=MibTableColumn
chmgrOConnSourceDsti=_ChmgrOConnSourceDsti_Object((1,3,6,1,4,1,2928,6,2,14,1,4,2,1,10),_ChmgrOConnSourceDsti_Type())
chmgrOConnSourceDsti.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOConnSourceDsti.setStatus(_A)
_ChmgrOConnStatusLastChanged_Type=TimeStamp
_ChmgrOConnStatusLastChanged_Object=MibTableColumn
chmgrOConnStatusLastChanged=_ChmgrOConnStatusLastChanged_Object((1,3,6,1,4,1,2928,6,2,14,1,4,2,1,11),_ChmgrOConnStatusLastChanged_Type())
chmgrOConnStatusLastChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOConnStatusLastChanged.setStatus(_A)
class _ChmgrOConnAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_ChmgrOConnAdminStatus_Type.__name__=_H
_ChmgrOConnAdminStatus_Object=MibTableColumn
chmgrOConnAdminStatus=_ChmgrOConnAdminStatus_Object((1,3,6,1,4,1,2928,6,2,14,1,4,2,1,12),_ChmgrOConnAdminStatus_Type())
chmgrOConnAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOConnAdminStatus.setStatus(_A)
class _ChmgrOConnOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5)));namedValues=NamedValues(*((_I,1),(_J,2),('partial',3),(_X,5)))
_ChmgrOConnOperStatus_Type.__name__=_H
_ChmgrOConnOperStatus_Object=MibTableColumn
chmgrOConnOperStatus=_ChmgrOConnOperStatus_Object((1,3,6,1,4,1,2928,6,2,14,1,4,2,1,13),_ChmgrOConnOperStatus_Type())
chmgrOConnOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOConnOperStatus.setStatus(_A)
class _ChmgrOConnReestablish_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Y,0),(_Z,1)))
_ChmgrOConnReestablish_Type.__name__=_H
_ChmgrOConnReestablish_Object=MibTableColumn
chmgrOConnReestablish=_ChmgrOConnReestablish_Object((1,3,6,1,4,1,2928,6,2,14,1,4,2,1,14),_ChmgrOConnReestablish_Type())
chmgrOConnReestablish.setMaxAccess(_D)
if mibBuilder.loadTexts:chmgrOConnReestablish.setStatus(_A)
_ChmgrOConnForceSourceRoute_Type=Unsigned32
_ChmgrOConnForceSourceRoute_Object=MibTableColumn
chmgrOConnForceSourceRoute=_ChmgrOConnForceSourceRoute_Object((1,3,6,1,4,1,2928,6,2,14,1,4,2,1,15),_ChmgrOConnForceSourceRoute_Type())
chmgrOConnForceSourceRoute.setMaxAccess(_D)
if mibBuilder.loadTexts:chmgrOConnForceSourceRoute.setStatus(_A)
_ChmgrOConnDcpVersion_Type=DcpVersion
_ChmgrOConnDcpVersion_Object=MibTableColumn
chmgrOConnDcpVersion=_ChmgrOConnDcpVersion_Object((1,3,6,1,4,1,2928,6,2,14,1,4,2,1,16),_ChmgrOConnDcpVersion_Type())
chmgrOConnDcpVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOConnDcpVersion.setStatus(_A)
_ChmgrODestinationTable_Object=MibTable
chmgrODestinationTable=_ChmgrODestinationTable_Object((1,3,6,1,4,1,2928,6,2,14,1,4,3))
if mibBuilder.loadTexts:chmgrODestinationTable.setStatus(_A)
_ChmgrODestinationEntry_Object=MibTableRow
chmgrODestinationEntry=_ChmgrODestinationEntry_Object((1,3,6,1,4,1,2928,6,2,14,1,4,3,1))
chmgrODestinationEntry.setIndexNames((0,_C,_M),(0,_C,_L))
if mibBuilder.loadTexts:chmgrODestinationEntry.setStatus(_A)
_ChmgrODestDestinationAddress_Type=DtmNode
_ChmgrODestDestinationAddress_Object=MibTableColumn
chmgrODestDestinationAddress=_ChmgrODestDestinationAddress_Object((1,3,6,1,4,1,2928,6,2,14,1,4,3,1,1),_ChmgrODestDestinationAddress_Type())
chmgrODestDestinationAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrODestDestinationAddress.setStatus(_A)
_ChmgrODestDestinationDsti_Type=Dsti
_ChmgrODestDestinationDsti_Object=MibTableColumn
chmgrODestDestinationDsti=_ChmgrODestDestinationDsti_Object((1,3,6,1,4,1,2928,6,2,14,1,4,3,1,2),_ChmgrODestDestinationDsti_Type())
chmgrODestDestinationDsti.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrODestDestinationDsti.setStatus(_A)
_ChmgrOChannelTable_Object=MibTable
chmgrOChannelTable=_ChmgrOChannelTable_Object((1,3,6,1,4,1,2928,6,2,14,1,4,4))
if mibBuilder.loadTexts:chmgrOChannelTable.setStatus(_A)
_ChmgrOChannelEntry_Object=MibTableRow
chmgrOChannelEntry=_ChmgrOChannelEntry_Object((1,3,6,1,4,1,2928,6,2,14,1,4,4,1))
chmgrOChannelEntry.setIndexNames((0,_C,_M),(0,_C,_L),(0,_C,_R))
if mibBuilder.loadTexts:chmgrOChannelEntry.setStatus(_A)
_ChmgrOChanSourceRouteIndex_Type=Unsigned32
_ChmgrOChanSourceRouteIndex_Object=MibTableColumn
chmgrOChanSourceRouteIndex=_ChmgrOChanSourceRouteIndex_Object((1,3,6,1,4,1,2928,6,2,14,1,4,4,1,1),_ChmgrOChanSourceRouteIndex_Type())
chmgrOChanSourceRouteIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOChanSourceRouteIndex.setStatus(_A)
_ChmgrOChanChannelId_Type=ChannelId
_ChmgrOChanChannelId_Object=MibTableColumn
chmgrOChanChannelId=_ChmgrOChanChannelId_Object((1,3,6,1,4,1,2928,6,2,14,1,4,4,1,2),_ChmgrOChanChannelId_Type())
chmgrOChanChannelId.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOChanChannelId.setStatus(_A)
_ChmgrOChanErrorMessage_Type=SnmpAdminString
_ChmgrOChanErrorMessage_Object=MibTableColumn
chmgrOChanErrorMessage=_ChmgrOChanErrorMessage_Object((1,3,6,1,4,1,2928,6,2,14,1,4,4,1,3),_ChmgrOChanErrorMessage_Type())
chmgrOChanErrorMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOChanErrorMessage.setStatus(_A)
_ChmgrOChanErrorAddress_Type=DtmNode
_ChmgrOChanErrorAddress_Object=MibTableColumn
chmgrOChanErrorAddress=_ChmgrOChanErrorAddress_Object((1,3,6,1,4,1,2928,6,2,14,1,4,4,1,4),_ChmgrOChanErrorAddress_Type())
chmgrOChanErrorAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOChanErrorAddress.setStatus(_A)
class _ChmgrOChanOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_ChmgrOChanOperStatus_Type.__name__=_H
_ChmgrOChanOperStatus_Object=MibTableColumn
chmgrOChanOperStatus=_ChmgrOChanOperStatus_Object((1,3,6,1,4,1,2928,6,2,14,1,4,4,1,5),_ChmgrOChanOperStatus_Type())
chmgrOChanOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOChanOperStatus.setStatus(_A)
_ChmgrOChanStatusChanged_Type=TimeStamp
_ChmgrOChanStatusChanged_Object=MibTableColumn
chmgrOChanStatusChanged=_ChmgrOChanStatusChanged_Object((1,3,6,1,4,1,2928,6,2,14,1,4,4,1,6),_ChmgrOChanStatusChanged_Type())
chmgrOChanStatusChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOChanStatusChanged.setStatus(_A)
class _ChmgrOChanReestablish_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Y,0),(_Z,1)))
_ChmgrOChanReestablish_Type.__name__=_H
_ChmgrOChanReestablish_Object=MibTableColumn
chmgrOChanReestablish=_ChmgrOChanReestablish_Object((1,3,6,1,4,1,2928,6,2,14,1,4,4,1,7),_ChmgrOChanReestablish_Type())
chmgrOChanReestablish.setMaxAccess(_D)
if mibBuilder.loadTexts:chmgrOChanReestablish.setStatus(_A)
_ChmgrTConnectionGroup_ObjectIdentity=ObjectIdentity
chmgrTConnectionGroup=_ChmgrTConnectionGroup_ObjectIdentity((1,3,6,1,4,1,2928,6,2,14,1,5))
_ChmgrTConnectionTimeStamp_Type=TimeStamp
_ChmgrTConnectionTimeStamp_Object=MibScalar
chmgrTConnectionTimeStamp=_ChmgrTConnectionTimeStamp_Object((1,3,6,1,4,1,2928,6,2,14,1,5,1),_ChmgrTConnectionTimeStamp_Type())
chmgrTConnectionTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTConnectionTimeStamp.setStatus(_A)
_ChmgrTConnectionTable_Object=MibTable
chmgrTConnectionTable=_ChmgrTConnectionTable_Object((1,3,6,1,4,1,2928,6,2,14,1,5,2))
if mibBuilder.loadTexts:chmgrTConnectionTable.setStatus(_A)
_ChmgrTConnectionEntry_Object=MibTableRow
chmgrTConnectionEntry=_ChmgrTConnectionEntry_Object((1,3,6,1,4,1,2928,6,2,14,1,5,2,1))
chmgrTConnectionEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:chmgrTConnectionEntry.setStatus(_A)
_ChmgrTConnIndex_Type=Unsigned32
_ChmgrTConnIndex_Object=MibTableColumn
chmgrTConnIndex=_ChmgrTConnIndex_Object((1,3,6,1,4,1,2928,6,2,14,1,5,2,1,1),_ChmgrTConnIndex_Type())
chmgrTConnIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:chmgrTConnIndex.setStatus(_A)
_ChmgrTConnCustomerId_Type=Unsigned32
_ChmgrTConnCustomerId_Object=MibTableColumn
chmgrTConnCustomerId=_ChmgrTConnCustomerId_Object((1,3,6,1,4,1,2928,6,2,14,1,5,2,1,2),_ChmgrTConnCustomerId_Type())
chmgrTConnCustomerId.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTConnCustomerId.setStatus(_A)
class _ChmgrTConnNumberOfChannels_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_ChmgrTConnNumberOfChannels_Type.__name__=_F
_ChmgrTConnNumberOfChannels_Object=MibTableColumn
chmgrTConnNumberOfChannels=_ChmgrTConnNumberOfChannels_Object((1,3,6,1,4,1,2928,6,2,14,1,5,2,1,3),_ChmgrTConnNumberOfChannels_Type())
chmgrTConnNumberOfChannels.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTConnNumberOfChannels.setStatus(_A)
class _ChmgrTConnActiveChannel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_ChmgrTConnActiveChannel_Type.__name__=_F
_ChmgrTConnActiveChannel_Object=MibTableColumn
chmgrTConnActiveChannel=_ChmgrTConnActiveChannel_Object((1,3,6,1,4,1,2928,6,2,14,1,5,2,1,4),_ChmgrTConnActiveChannel_Type())
chmgrTConnActiveChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTConnActiveChannel.setStatus(_A)
_ChmgrTConnServiceReference_Type=RowPointer
_ChmgrTConnServiceReference_Object=MibTableColumn
chmgrTConnServiceReference=_ChmgrTConnServiceReference_Object((1,3,6,1,4,1,2928,6,2,14,1,5,2,1,5),_ChmgrTConnServiceReference_Type())
chmgrTConnServiceReference.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTConnServiceReference.setStatus(_A)
class _ChmgrTConnAllocatedSlots_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8389))
_ChmgrTConnAllocatedSlots_Type.__name__=_K
_ChmgrTConnAllocatedSlots_Object=MibTableColumn
chmgrTConnAllocatedSlots=_ChmgrTConnAllocatedSlots_Object((1,3,6,1,4,1,2928,6,2,14,1,5,2,1,6),_ChmgrTConnAllocatedSlots_Type())
chmgrTConnAllocatedSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTConnAllocatedSlots.setStatus(_A)
_ChmgrTConnAllocatedSlotsChanged_Type=TimeStamp
_ChmgrTConnAllocatedSlotsChanged_Object=MibTableColumn
chmgrTConnAllocatedSlotsChanged=_ChmgrTConnAllocatedSlotsChanged_Object((1,3,6,1,4,1,2928,6,2,14,1,5,2,1,7),_ChmgrTConnAllocatedSlotsChanged_Type())
chmgrTConnAllocatedSlotsChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTConnAllocatedSlotsChanged.setStatus(_A)
_ChmgrTConnDcapType_Type=DcapType
_ChmgrTConnDcapType_Object=MibTableColumn
chmgrTConnDcapType=_ChmgrTConnDcapType_Object((1,3,6,1,4,1,2928,6,2,14,1,5,2,1,8),_ChmgrTConnDcapType_Type())
chmgrTConnDcapType.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTConnDcapType.setStatus(_A)
_ChmgrTConnDst_Type=Dst
_ChmgrTConnDst_Object=MibTableColumn
chmgrTConnDst=_ChmgrTConnDst_Object((1,3,6,1,4,1,2928,6,2,14,1,5,2,1,9),_ChmgrTConnDst_Type())
chmgrTConnDst.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTConnDst.setStatus(_A)
_ChmgrTConnSourceDsti_Type=Dsti
_ChmgrTConnSourceDsti_Object=MibTableColumn
chmgrTConnSourceDsti=_ChmgrTConnSourceDsti_Object((1,3,6,1,4,1,2928,6,2,14,1,5,2,1,10),_ChmgrTConnSourceDsti_Type())
chmgrTConnSourceDsti.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTConnSourceDsti.setStatus(_A)
_ChmgrTConnSourceAddress_Type=DtmNode
_ChmgrTConnSourceAddress_Object=MibTableColumn
chmgrTConnSourceAddress=_ChmgrTConnSourceAddress_Object((1,3,6,1,4,1,2928,6,2,14,1,5,2,1,11),_ChmgrTConnSourceAddress_Type())
chmgrTConnSourceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTConnSourceAddress.setStatus(_A)
_ChmgrTConnDestinationDsti_Type=Dsti
_ChmgrTConnDestinationDsti_Object=MibTableColumn
chmgrTConnDestinationDsti=_ChmgrTConnDestinationDsti_Object((1,3,6,1,4,1,2928,6,2,14,1,5,2,1,12),_ChmgrTConnDestinationDsti_Type())
chmgrTConnDestinationDsti.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTConnDestinationDsti.setStatus(_A)
_ChmgrTConnDestinationAddress_Type=DtmNode
_ChmgrTConnDestinationAddress_Object=MibTableColumn
chmgrTConnDestinationAddress=_ChmgrTConnDestinationAddress_Object((1,3,6,1,4,1,2928,6,2,14,1,5,2,1,13),_ChmgrTConnDestinationAddress_Type())
chmgrTConnDestinationAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTConnDestinationAddress.setStatus(_A)
_ChmgrTConnStatusLastChanged_Type=TimeStamp
_ChmgrTConnStatusLastChanged_Object=MibTableColumn
chmgrTConnStatusLastChanged=_ChmgrTConnStatusLastChanged_Object((1,3,6,1,4,1,2928,6,2,14,1,5,2,1,14),_ChmgrTConnStatusLastChanged_Type())
chmgrTConnStatusLastChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTConnStatusLastChanged.setStatus(_A)
class _ChmgrTConnAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_ChmgrTConnAdminStatus_Type.__name__=_H
_ChmgrTConnAdminStatus_Object=MibTableColumn
chmgrTConnAdminStatus=_ChmgrTConnAdminStatus_Object((1,3,6,1,4,1,2928,6,2,14,1,5,2,1,15),_ChmgrTConnAdminStatus_Type())
chmgrTConnAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTConnAdminStatus.setStatus(_A)
class _ChmgrTConnOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5)));namedValues=NamedValues(*((_I,1),(_J,2),(_X,5)))
_ChmgrTConnOperStatus_Type.__name__=_H
_ChmgrTConnOperStatus_Object=MibTableColumn
chmgrTConnOperStatus=_ChmgrTConnOperStatus_Object((1,3,6,1,4,1,2928,6,2,14,1,5,2,1,16),_ChmgrTConnOperStatus_Type())
chmgrTConnOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTConnOperStatus.setStatus(_A)
_ChmgrTConnDcpVersion_Type=DcpVersion
_ChmgrTConnDcpVersion_Object=MibTableColumn
chmgrTConnDcpVersion=_ChmgrTConnDcpVersion_Object((1,3,6,1,4,1,2928,6,2,14,1,5,2,1,17),_ChmgrTConnDcpVersion_Type())
chmgrTConnDcpVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTConnDcpVersion.setStatus(_A)
_ChmgrTChannelTable_Object=MibTable
chmgrTChannelTable=_ChmgrTChannelTable_Object((1,3,6,1,4,1,2928,6,2,14,1,5,3))
if mibBuilder.loadTexts:chmgrTChannelTable.setStatus(_A)
_ChmgrTChannelEntry_Object=MibTableRow
chmgrTChannelEntry=_ChmgrTChannelEntry_Object((1,3,6,1,4,1,2928,6,2,14,1,5,3,1))
chmgrTChannelEntry.setIndexNames((0,_C,_N),(0,_C,_a))
if mibBuilder.loadTexts:chmgrTChannelEntry.setStatus(_A)
class _ChmgrTChanIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_ChmgrTChanIndex_Type.__name__=_F
_ChmgrTChanIndex_Object=MibTableColumn
chmgrTChanIndex=_ChmgrTChanIndex_Object((1,3,6,1,4,1,2928,6,2,14,1,5,3,1,1),_ChmgrTChanIndex_Type())
chmgrTChanIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:chmgrTChanIndex.setStatus(_A)
_ChmgrTChanChannelId_Type=ChannelId
_ChmgrTChanChannelId_Object=MibTableColumn
chmgrTChanChannelId=_ChmgrTChanChannelId_Object((1,3,6,1,4,1,2928,6,2,14,1,5,3,1,2),_ChmgrTChanChannelId_Type())
chmgrTChanChannelId.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTChanChannelId.setStatus(_A)
_ChmgrTChanCreated_Type=TimeStamp
_ChmgrTChanCreated_Object=MibTableColumn
chmgrTChanCreated=_ChmgrTChanCreated_Object((1,3,6,1,4,1,2928,6,2,14,1,5,3,1,3),_ChmgrTChanCreated_Type())
chmgrTChanCreated.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTChanCreated.setStatus(_A)
_ChmgrStatisticsGroup_ObjectIdentity=ObjectIdentity
chmgrStatisticsGroup=_ChmgrStatisticsGroup_ObjectIdentity((1,3,6,1,4,1,2928,6,2,14,1,6))
_ChmgrOStatDcap1Table_Object=MibTable
chmgrOStatDcap1Table=_ChmgrOStatDcap1Table_Object((1,3,6,1,4,1,2928,6,2,14,1,6,1))
if mibBuilder.loadTexts:chmgrOStatDcap1Table.setStatus(_A)
_ChmgrOStatDcap1Entry_Object=MibTableRow
chmgrOStatDcap1Entry=_ChmgrOStatDcap1Entry_Object((1,3,6,1,4,1,2928,6,2,14,1,6,1,1))
chmgrOStatDcap1Entry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:chmgrOStatDcap1Entry.setStatus(_A)
_ChmgrOStatDcap1Octets_Type=Counter32
_ChmgrOStatDcap1Octets_Object=MibTableColumn
chmgrOStatDcap1Octets=_ChmgrOStatDcap1Octets_Object((1,3,6,1,4,1,2928,6,2,14,1,6,1,1,1),_ChmgrOStatDcap1Octets_Type())
chmgrOStatDcap1Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOStatDcap1Octets.setStatus(_A)
_ChmgrOStatDcap1Packets_Type=Counter32
_ChmgrOStatDcap1Packets_Object=MibTableColumn
chmgrOStatDcap1Packets=_ChmgrOStatDcap1Packets_Object((1,3,6,1,4,1,2928,6,2,14,1,6,1,1,2),_ChmgrOStatDcap1Packets_Type())
chmgrOStatDcap1Packets.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOStatDcap1Packets.setStatus(_A)
_ChmgrOStatDcap1UtilizedBps_Type=Gauge32
_ChmgrOStatDcap1UtilizedBps_Object=MibTableColumn
chmgrOStatDcap1UtilizedBps=_ChmgrOStatDcap1UtilizedBps_Object((1,3,6,1,4,1,2928,6,2,14,1,6,1,1,3),_ChmgrOStatDcap1UtilizedBps_Type())
chmgrOStatDcap1UtilizedBps.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOStatDcap1UtilizedBps.setStatus(_A)
_ChmgrOStatDcap1DiscardOctets_Type=Counter32
_ChmgrOStatDcap1DiscardOctets_Object=MibTableColumn
chmgrOStatDcap1DiscardOctets=_ChmgrOStatDcap1DiscardOctets_Object((1,3,6,1,4,1,2928,6,2,14,1,6,1,1,4),_ChmgrOStatDcap1DiscardOctets_Type())
chmgrOStatDcap1DiscardOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOStatDcap1DiscardOctets.setStatus(_A)
_ChmgrOStatDcap1DiscardPackets_Type=Counter32
_ChmgrOStatDcap1DiscardPackets_Object=MibTableColumn
chmgrOStatDcap1DiscardPackets=_ChmgrOStatDcap1DiscardPackets_Object((1,3,6,1,4,1,2928,6,2,14,1,6,1,1,5),_ChmgrOStatDcap1DiscardPackets_Type())
chmgrOStatDcap1DiscardPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOStatDcap1DiscardPackets.setStatus(_A)
_ChmgrOStatDcap1Bitrate_Type=Counter64
_ChmgrOStatDcap1Bitrate_Object=MibTableColumn
chmgrOStatDcap1Bitrate=_ChmgrOStatDcap1Bitrate_Object((1,3,6,1,4,1,2928,6,2,14,1,6,1,1,6),_ChmgrOStatDcap1Bitrate_Type())
chmgrOStatDcap1Bitrate.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOStatDcap1Bitrate.setStatus(_A)
class _ChmgrOStatDcap1Load_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ChmgrOStatDcap1Load_Type.__name__=_F
_ChmgrOStatDcap1Load_Object=MibTableColumn
chmgrOStatDcap1Load=_ChmgrOStatDcap1Load_Object((1,3,6,1,4,1,2928,6,2,14,1,6,1,1,7),_ChmgrOStatDcap1Load_Type())
chmgrOStatDcap1Load.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrOStatDcap1Load.setStatus(_A)
_ChmgrTStatDcap1Table_Object=MibTable
chmgrTStatDcap1Table=_ChmgrTStatDcap1Table_Object((1,3,6,1,4,1,2928,6,2,14,1,6,2))
if mibBuilder.loadTexts:chmgrTStatDcap1Table.setStatus(_A)
_ChmgrTStatDcap1Entry_Object=MibTableRow
chmgrTStatDcap1Entry=_ChmgrTStatDcap1Entry_Object((1,3,6,1,4,1,2928,6,2,14,1,6,2,1))
chmgrTStatDcap1Entry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:chmgrTStatDcap1Entry.setStatus(_A)
_ChmgrTStatDcap1Octets_Type=Counter32
_ChmgrTStatDcap1Octets_Object=MibTableColumn
chmgrTStatDcap1Octets=_ChmgrTStatDcap1Octets_Object((1,3,6,1,4,1,2928,6,2,14,1,6,2,1,1),_ChmgrTStatDcap1Octets_Type())
chmgrTStatDcap1Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTStatDcap1Octets.setStatus(_A)
_ChmgrTStatDcap1Packets_Type=Counter32
_ChmgrTStatDcap1Packets_Object=MibTableColumn
chmgrTStatDcap1Packets=_ChmgrTStatDcap1Packets_Object((1,3,6,1,4,1,2928,6,2,14,1,6,2,1,2),_ChmgrTStatDcap1Packets_Type())
chmgrTStatDcap1Packets.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTStatDcap1Packets.setStatus(_A)
_ChmgrTStatDcap1UtilizedBps_Type=Gauge32
_ChmgrTStatDcap1UtilizedBps_Object=MibTableColumn
chmgrTStatDcap1UtilizedBps=_ChmgrTStatDcap1UtilizedBps_Object((1,3,6,1,4,1,2928,6,2,14,1,6,2,1,3),_ChmgrTStatDcap1UtilizedBps_Type())
chmgrTStatDcap1UtilizedBps.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTStatDcap1UtilizedBps.setStatus(_A)
_ChmgrTStatDcap1DiscardOctets_Type=Counter32
_ChmgrTStatDcap1DiscardOctets_Object=MibTableColumn
chmgrTStatDcap1DiscardOctets=_ChmgrTStatDcap1DiscardOctets_Object((1,3,6,1,4,1,2928,6,2,14,1,6,2,1,4),_ChmgrTStatDcap1DiscardOctets_Type())
chmgrTStatDcap1DiscardOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTStatDcap1DiscardOctets.setStatus(_A)
_ChmgrTStatDcap1DiscardPackets_Type=Counter32
_ChmgrTStatDcap1DiscardPackets_Object=MibTableColumn
chmgrTStatDcap1DiscardPackets=_ChmgrTStatDcap1DiscardPackets_Object((1,3,6,1,4,1,2928,6,2,14,1,6,2,1,5),_ChmgrTStatDcap1DiscardPackets_Type())
chmgrTStatDcap1DiscardPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTStatDcap1DiscardPackets.setStatus(_A)
_ChmgrTStatDcap1ErrorCRC_Type=Counter32
_ChmgrTStatDcap1ErrorCRC_Object=MibTableColumn
chmgrTStatDcap1ErrorCRC=_ChmgrTStatDcap1ErrorCRC_Object((1,3,6,1,4,1,2928,6,2,14,1,6,2,1,6),_ChmgrTStatDcap1ErrorCRC_Type())
chmgrTStatDcap1ErrorCRC.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTStatDcap1ErrorCRC.setStatus(_A)
_ChmgrTStatDcap1ErrorLods_Type=Counter32
_ChmgrTStatDcap1ErrorLods_Object=MibTableColumn
chmgrTStatDcap1ErrorLods=_ChmgrTStatDcap1ErrorLods_Object((1,3,6,1,4,1,2928,6,2,14,1,6,2,1,7),_ChmgrTStatDcap1ErrorLods_Type())
chmgrTStatDcap1ErrorLods.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTStatDcap1ErrorLods.setStatus(_A)
_ChmgrTStatDcap1Bitrate_Type=Counter64
_ChmgrTStatDcap1Bitrate_Object=MibTableColumn
chmgrTStatDcap1Bitrate=_ChmgrTStatDcap1Bitrate_Object((1,3,6,1,4,1,2928,6,2,14,1,6,2,1,8),_ChmgrTStatDcap1Bitrate_Type())
chmgrTStatDcap1Bitrate.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTStatDcap1Bitrate.setStatus(_A)
class _ChmgrTStatDcap1Load_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ChmgrTStatDcap1Load_Type.__name__=_F
_ChmgrTStatDcap1Load_Object=MibTableColumn
chmgrTStatDcap1Load=_ChmgrTStatDcap1Load_Object((1,3,6,1,4,1,2928,6,2,14,1,6,2,1,9),_ChmgrTStatDcap1Load_Type())
chmgrTStatDcap1Load.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTStatDcap1Load.setStatus(_A)
_ChmgrTStatPMReferenceTable_Object=MibTable
chmgrTStatPMReferenceTable=_ChmgrTStatPMReferenceTable_Object((1,3,6,1,4,1,2928,6,2,14,1,6,3))
if mibBuilder.loadTexts:chmgrTStatPMReferenceTable.setStatus(_T)
_ChmgrTStatPMReferenceEntry_Object=MibTableRow
chmgrTStatPMReferenceEntry=_ChmgrTStatPMReferenceEntry_Object((1,3,6,1,4,1,2928,6,2,14,1,6,3,1))
chmgrTStatPMReferenceEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:chmgrTStatPMReferenceEntry.setStatus(_T)
_ChmgrTStatPMReference_Type=RowPointer
_ChmgrTStatPMReference_Object=MibTableColumn
chmgrTStatPMReference=_ChmgrTStatPMReference_Object((1,3,6,1,4,1,2928,6,2,14,1,6,3,1,1),_ChmgrTStatPMReference_Type())
chmgrTStatPMReference.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrTStatPMReference.setStatus(_T)
_ChmgrChannelGroup_ObjectIdentity=ObjectIdentity
chmgrChannelGroup=_ChmgrChannelGroup_ObjectIdentity((1,3,6,1,4,1,2928,6,2,14,1,7))
_ChmgrChannelTable_Object=MibTable
chmgrChannelTable=_ChmgrChannelTable_Object((1,3,6,1,4,1,2928,6,2,14,1,7,1))
if mibBuilder.loadTexts:chmgrChannelTable.setStatus(_A)
_ChmgrChannelEntry_Object=MibTableRow
chmgrChannelEntry=_ChmgrChannelEntry_Object((1,3,6,1,4,1,2928,6,2,14,1,7,1,1))
chmgrChannelEntry.setIndexNames((0,_C,_b),(0,_C,_c),(0,_C,_d),(0,_C,_e))
if mibBuilder.loadTexts:chmgrChannelEntry.setStatus(_A)
_ChmgrChanSourceMacAddress_Type=MacAddress
_ChmgrChanSourceMacAddress_Object=MibTableColumn
chmgrChanSourceMacAddress=_ChmgrChanSourceMacAddress_Object((1,3,6,1,4,1,2928,6,2,14,1,7,1,1,1),_ChmgrChanSourceMacAddress_Type())
chmgrChanSourceMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:chmgrChanSourceMacAddress.setStatus(_A)
_ChmgrChanChannelId_Type=ChannelId
_ChmgrChanChannelId_Object=MibTableColumn
chmgrChanChannelId=_ChmgrChanChannelId_Object((1,3,6,1,4,1,2928,6,2,14,1,7,1,1,2),_ChmgrChanChannelId_Type())
chmgrChanChannelId.setMaxAccess(_G)
if mibBuilder.loadTexts:chmgrChanChannelId.setStatus(_A)
_ChmgrChanOutgoingIfBoard_Type=Unsigned32
_ChmgrChanOutgoingIfBoard_Object=MibTableColumn
chmgrChanOutgoingIfBoard=_ChmgrChanOutgoingIfBoard_Object((1,3,6,1,4,1,2928,6,2,14,1,7,1,1,3),_ChmgrChanOutgoingIfBoard_Type())
chmgrChanOutgoingIfBoard.setMaxAccess(_G)
if mibBuilder.loadTexts:chmgrChanOutgoingIfBoard.setStatus(_A)
_ChmgrChanOutgoingIfPort_Type=Unsigned32
_ChmgrChanOutgoingIfPort_Object=MibTableColumn
chmgrChanOutgoingIfPort=_ChmgrChanOutgoingIfPort_Object((1,3,6,1,4,1,2928,6,2,14,1,7,1,1,4),_ChmgrChanOutgoingIfPort_Type())
chmgrChanOutgoingIfPort.setMaxAccess(_G)
if mibBuilder.loadTexts:chmgrChanOutgoingIfPort.setStatus(_A)
_ChmgrChanOutgoingIfMacAddress_Type=MacAddress
_ChmgrChanOutgoingIfMacAddress_Object=MibTableColumn
chmgrChanOutgoingIfMacAddress=_ChmgrChanOutgoingIfMacAddress_Object((1,3,6,1,4,1,2928,6,2,14,1,7,1,1,5),_ChmgrChanOutgoingIfMacAddress_Type())
chmgrChanOutgoingIfMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrChanOutgoingIfMacAddress.setStatus(_A)
_ChmgrChanNextHopMacAddress_Type=MacAddress
_ChmgrChanNextHopMacAddress_Object=MibTableColumn
chmgrChanNextHopMacAddress=_ChmgrChanNextHopMacAddress_Object((1,3,6,1,4,1,2928,6,2,14,1,7,1,1,6),_ChmgrChanNextHopMacAddress_Type())
chmgrChanNextHopMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrChanNextHopMacAddress.setStatus(_A)
_ChmgrChanNextHopDtmAddress_Type=DtmAddress
_ChmgrChanNextHopDtmAddress_Object=MibTableColumn
chmgrChanNextHopDtmAddress=_ChmgrChanNextHopDtmAddress_Object((1,3,6,1,4,1,2928,6,2,14,1,7,1,1,7),_ChmgrChanNextHopDtmAddress_Type())
chmgrChanNextHopDtmAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrChanNextHopDtmAddress.setStatus(_A)
_ChmgrChanIncomingIfBoard_Type=Unsigned32
_ChmgrChanIncomingIfBoard_Object=MibTableColumn
chmgrChanIncomingIfBoard=_ChmgrChanIncomingIfBoard_Object((1,3,6,1,4,1,2928,6,2,14,1,7,1,1,8),_ChmgrChanIncomingIfBoard_Type())
chmgrChanIncomingIfBoard.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrChanIncomingIfBoard.setStatus(_A)
_ChmgrChanIncomingIfPort_Type=Unsigned32
_ChmgrChanIncomingIfPort_Object=MibTableColumn
chmgrChanIncomingIfPort=_ChmgrChanIncomingIfPort_Object((1,3,6,1,4,1,2928,6,2,14,1,7,1,1,9),_ChmgrChanIncomingIfPort_Type())
chmgrChanIncomingIfPort.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrChanIncomingIfPort.setStatus(_A)
_ChmgrChanSourceDtmAddress_Type=DtmAddress
_ChmgrChanSourceDtmAddress_Object=MibTableColumn
chmgrChanSourceDtmAddress=_ChmgrChanSourceDtmAddress_Object((1,3,6,1,4,1,2928,6,2,14,1,7,1,1,10),_ChmgrChanSourceDtmAddress_Type())
chmgrChanSourceDtmAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrChanSourceDtmAddress.setStatus(_A)
_ChmgrChanDst_Type=Dst
_ChmgrChanDst_Object=MibTableColumn
chmgrChanDst=_ChmgrChanDst_Object((1,3,6,1,4,1,2928,6,2,14,1,7,1,1,11),_ChmgrChanDst_Type())
chmgrChanDst.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrChanDst.setStatus(_A)
_ChmgrChanSourceDsti_Type=Dsti
_ChmgrChanSourceDsti_Object=MibTableColumn
chmgrChanSourceDsti=_ChmgrChanSourceDsti_Object((1,3,6,1,4,1,2928,6,2,14,1,7,1,1,12),_ChmgrChanSourceDsti_Type())
chmgrChanSourceDsti.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrChanSourceDsti.setStatus(_A)
_ChmgrChanIsMulticast_Type=TruthValue
_ChmgrChanIsMulticast_Object=MibTableColumn
chmgrChanIsMulticast=_ChmgrChanIsMulticast_Object((1,3,6,1,4,1,2928,6,2,14,1,7,1,1,13),_ChmgrChanIsMulticast_Type())
chmgrChanIsMulticast.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrChanIsMulticast.setStatus(_A)
_ChmgrChanCapacity_Type=Unsigned32
_ChmgrChanCapacity_Object=MibTableColumn
chmgrChanCapacity=_ChmgrChanCapacity_Object((1,3,6,1,4,1,2928,6,2,14,1,7,1,1,14),_ChmgrChanCapacity_Type())
chmgrChanCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrChanCapacity.setStatus(_A)
_ChmgrChanDestDsti_Type=Dsti
_ChmgrChanDestDsti_Object=MibTableColumn
chmgrChanDestDsti=_ChmgrChanDestDsti_Object((1,3,6,1,4,1,2928,6,2,14,1,7,1,1,15),_ChmgrChanDestDsti_Type())
chmgrChanDestDsti.setMaxAccess(_B)
if mibBuilder.loadTexts:chmgrChanDestDsti.setStatus(_A)
_ChmgrNotifications_ObjectIdentity=ObjectIdentity
chmgrNotifications=_ChmgrNotifications_ObjectIdentity((1,3,6,1,4,1,2928,6,2,14,2))
_ChmgrConformance_ObjectIdentity=ObjectIdentity
chmgrConformance=_ChmgrConformance_ObjectIdentity((1,3,6,1,4,1,2928,6,2,14,3))
mibBuilder.exportSymbols(_C,**{'Dst':Dst,'Dsti':Dsti,'ChannelId':ChannelId,'DcapType':DcapType,_U:DtmNode,'DcpVersion':DcpVersion,'netiChmgrMIB':netiChmgrMIB,'chmgrObjects':chmgrObjects,'chmgrODescriptionGroup':chmgrODescriptionGroup,'chmgrODescriptionTimeStamp':chmgrODescriptionTimeStamp,'chmgrODescriptionTable':chmgrODescriptionTable,'chmgrODescriptionEntry':chmgrODescriptionEntry,_O:chmgrODescrIndex,'chmgrODescrType':chmgrODescrType,'chmgrODescrCapabilities':chmgrODescrCapabilities,'chmgrODescrCustomerId':chmgrODescrCustomerId,'chmgrODescrServiceReference':chmgrODescrServiceReference,'chmgrODescrAcceptableBps':chmgrODescrAcceptableBps,'chmgrODescrAcceptableSlots':chmgrODescrAcceptableSlots,'chmgrODescrRequestedBps':chmgrODescrRequestedBps,'chmgrODescrRequestedSlots':chmgrODescrRequestedSlots,'chmgrODescrReestablishMethod':chmgrODescrReestablishMethod,'chmgrODescrMinInterval':chmgrODescrMinInterval,'chmgrODescrMaxInterval':chmgrODescrMaxInterval,'chmgrODescrEstablish':chmgrODescrEstablish,'chmgrODescrNextDestTableIndex':chmgrODescrNextDestTableIndex,'chmgrODescrPrecedence':chmgrODescrPrecedence,'chmgrODescrSuppressAlarms':chmgrODescrSuppressAlarms,'chmgrODescrAcceptableMbps':chmgrODescrAcceptableMbps,'chmgrODescrRequestedMbps':chmgrODescrRequestedMbps,'chmgrODescrRequestedDcpVersion':chmgrODescrRequestedDcpVersion,'chmgrODescrOneHopSpareCapUtilization':chmgrODescrOneHopSpareCapUtilization,'chmgrODescrDestinationTable':chmgrODescrDestinationTable,'chmgrODescrDestinationEntry':chmgrODescrDestinationEntry,_L:chmgrODescrDestIndex,'chmgrODescrDestAddress':chmgrODescrDestAddress,'chmgrODescrDestDsti':chmgrODescrDestDsti,'chmgrODescrDestRowStatus':chmgrODescrDestRowStatus,'chmgrODescrDestAdminStatus':chmgrODescrDestAdminStatus,'chmgrODescrChannelTable':chmgrODescrChannelTable,'chmgrODescrChannelEntry':chmgrODescrChannelEntry,_R:chmgrODescrChanIndex,_V:chmgrODescrChanSourceRouteIndex,'chmgrODescrChanSourceRoute':chmgrODescrChanSourceRoute,'chmgrODescrChanRowStatus':chmgrODescrChanRowStatus,'chmgrTDescriptionGroup':chmgrTDescriptionGroup,'chmgrSourceRouteGroup':chmgrSourceRouteGroup,'chmgrSourceRouteTimeStamp':chmgrSourceRouteTimeStamp,'chmgrSourceRouteTable':chmgrSourceRouteTable,'chmgrSourceRouteEntry':chmgrSourceRouteEntry,_S:chmgrSourceRouteIndex,'chmgrSourceRouteName':chmgrSourceRouteName,'chmgrSourceRouteTypeOfRoute':chmgrSourceRouteTypeOfRoute,'chmgrSourceRouteFirstIfBoard':chmgrSourceRouteFirstIfBoard,'chmgrSourceRouteFirstIfPort':chmgrSourceRouteFirstIfPort,'chmgrSourceRouteRowStatus':chmgrSourceRouteRowStatus,'chmgrSourceRouteHopTable':chmgrSourceRouteHopTable,'chmgrSourceRouteHopEntry':chmgrSourceRouteHopEntry,_W:chmgrSourceRouteHopIndex,'chmgrSourceRouteHopAddress':chmgrSourceRouteHopAddress,'chmgrSourceRouteHopNextIfBoard':chmgrSourceRouteHopNextIfBoard,'chmgrSourceRouteHopNextIfPort':chmgrSourceRouteHopNextIfPort,'chmgrSourceRouteHopRowStatus':chmgrSourceRouteHopRowStatus,'chmgrOConnectionGroup':chmgrOConnectionGroup,'chmgrOConnectionTimeStamp':chmgrOConnectionTimeStamp,'chmgrOConnectionTable':chmgrOConnectionTable,'chmgrOConnectionEntry':chmgrOConnectionEntry,_M:chmgrOConnIndex,'chmgrOConnCustomerId':chmgrOConnCustomerId,'chmgrOConnODescrIndex':chmgrOConnODescrIndex,'chmgrOConnServiceReference':chmgrOConnServiceReference,'chmgrOConnAllocatedSlots':chmgrOConnAllocatedSlots,'chmgrOConnAllocatedSlotsChanged':chmgrOConnAllocatedSlotsChanged,'chmgrOConnDcapType':chmgrOConnDcapType,'chmgrOConnDst':chmgrOConnDst,'chmgrOConnSourceAddress':chmgrOConnSourceAddress,'chmgrOConnSourceDsti':chmgrOConnSourceDsti,'chmgrOConnStatusLastChanged':chmgrOConnStatusLastChanged,'chmgrOConnAdminStatus':chmgrOConnAdminStatus,'chmgrOConnOperStatus':chmgrOConnOperStatus,'chmgrOConnReestablish':chmgrOConnReestablish,'chmgrOConnForceSourceRoute':chmgrOConnForceSourceRoute,'chmgrOConnDcpVersion':chmgrOConnDcpVersion,'chmgrODestinationTable':chmgrODestinationTable,'chmgrODestinationEntry':chmgrODestinationEntry,'chmgrODestDestinationAddress':chmgrODestDestinationAddress,'chmgrODestDestinationDsti':chmgrODestDestinationDsti,'chmgrOChannelTable':chmgrOChannelTable,'chmgrOChannelEntry':chmgrOChannelEntry,'chmgrOChanSourceRouteIndex':chmgrOChanSourceRouteIndex,'chmgrOChanChannelId':chmgrOChanChannelId,'chmgrOChanErrorMessage':chmgrOChanErrorMessage,'chmgrOChanErrorAddress':chmgrOChanErrorAddress,'chmgrOChanOperStatus':chmgrOChanOperStatus,'chmgrOChanStatusChanged':chmgrOChanStatusChanged,'chmgrOChanReestablish':chmgrOChanReestablish,'chmgrTConnectionGroup':chmgrTConnectionGroup,'chmgrTConnectionTimeStamp':chmgrTConnectionTimeStamp,'chmgrTConnectionTable':chmgrTConnectionTable,'chmgrTConnectionEntry':chmgrTConnectionEntry,_N:chmgrTConnIndex,'chmgrTConnCustomerId':chmgrTConnCustomerId,'chmgrTConnNumberOfChannels':chmgrTConnNumberOfChannels,'chmgrTConnActiveChannel':chmgrTConnActiveChannel,'chmgrTConnServiceReference':chmgrTConnServiceReference,'chmgrTConnAllocatedSlots':chmgrTConnAllocatedSlots,'chmgrTConnAllocatedSlotsChanged':chmgrTConnAllocatedSlotsChanged,'chmgrTConnDcapType':chmgrTConnDcapType,'chmgrTConnDst':chmgrTConnDst,'chmgrTConnSourceDsti':chmgrTConnSourceDsti,'chmgrTConnSourceAddress':chmgrTConnSourceAddress,'chmgrTConnDestinationDsti':chmgrTConnDestinationDsti,'chmgrTConnDestinationAddress':chmgrTConnDestinationAddress,'chmgrTConnStatusLastChanged':chmgrTConnStatusLastChanged,'chmgrTConnAdminStatus':chmgrTConnAdminStatus,'chmgrTConnOperStatus':chmgrTConnOperStatus,'chmgrTConnDcpVersion':chmgrTConnDcpVersion,'chmgrTChannelTable':chmgrTChannelTable,'chmgrTChannelEntry':chmgrTChannelEntry,_a:chmgrTChanIndex,'chmgrTChanChannelId':chmgrTChanChannelId,'chmgrTChanCreated':chmgrTChanCreated,'chmgrStatisticsGroup':chmgrStatisticsGroup,'chmgrOStatDcap1Table':chmgrOStatDcap1Table,'chmgrOStatDcap1Entry':chmgrOStatDcap1Entry,'chmgrOStatDcap1Octets':chmgrOStatDcap1Octets,'chmgrOStatDcap1Packets':chmgrOStatDcap1Packets,'chmgrOStatDcap1UtilizedBps':chmgrOStatDcap1UtilizedBps,'chmgrOStatDcap1DiscardOctets':chmgrOStatDcap1DiscardOctets,'chmgrOStatDcap1DiscardPackets':chmgrOStatDcap1DiscardPackets,'chmgrOStatDcap1Bitrate':chmgrOStatDcap1Bitrate,'chmgrOStatDcap1Load':chmgrOStatDcap1Load,'chmgrTStatDcap1Table':chmgrTStatDcap1Table,'chmgrTStatDcap1Entry':chmgrTStatDcap1Entry,'chmgrTStatDcap1Octets':chmgrTStatDcap1Octets,'chmgrTStatDcap1Packets':chmgrTStatDcap1Packets,'chmgrTStatDcap1UtilizedBps':chmgrTStatDcap1UtilizedBps,'chmgrTStatDcap1DiscardOctets':chmgrTStatDcap1DiscardOctets,'chmgrTStatDcap1DiscardPackets':chmgrTStatDcap1DiscardPackets,'chmgrTStatDcap1ErrorCRC':chmgrTStatDcap1ErrorCRC,'chmgrTStatDcap1ErrorLods':chmgrTStatDcap1ErrorLods,'chmgrTStatDcap1Bitrate':chmgrTStatDcap1Bitrate,'chmgrTStatDcap1Load':chmgrTStatDcap1Load,'chmgrTStatPMReferenceTable':chmgrTStatPMReferenceTable,'chmgrTStatPMReferenceEntry':chmgrTStatPMReferenceEntry,'chmgrTStatPMReference':chmgrTStatPMReference,'chmgrChannelGroup':chmgrChannelGroup,'chmgrChannelTable':chmgrChannelTable,'chmgrChannelEntry':chmgrChannelEntry,_b:chmgrChanSourceMacAddress,_c:chmgrChanChannelId,_d:chmgrChanOutgoingIfBoard,_e:chmgrChanOutgoingIfPort,'chmgrChanOutgoingIfMacAddress':chmgrChanOutgoingIfMacAddress,'chmgrChanNextHopMacAddress':chmgrChanNextHopMacAddress,'chmgrChanNextHopDtmAddress':chmgrChanNextHopDtmAddress,'chmgrChanIncomingIfBoard':chmgrChanIncomingIfBoard,'chmgrChanIncomingIfPort':chmgrChanIncomingIfPort,'chmgrChanSourceDtmAddress':chmgrChanSourceDtmAddress,'chmgrChanDst':chmgrChanDst,'chmgrChanSourceDsti':chmgrChanSourceDsti,'chmgrChanIsMulticast':chmgrChanIsMulticast,'chmgrChanCapacity':chmgrChanCapacity,'chmgrChanDestDsti':chmgrChanDestDsti,'chmgrNotifications':chmgrNotifications,'chmgrConformance':chmgrConformance})