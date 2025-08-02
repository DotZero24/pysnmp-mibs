_K='bsNtpKeyId'
_J='not-accessible'
_I='bsNtpServerAddress'
_H='bsNtpServerAddressType'
_G='BAY-STACK-NTP-MIB'
_F='Integer32'
_E='TruthValue'
_D='DisplayString'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_D,'PhysAddress','RowStatus','TextualConvention',_E)
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackNtpMib=ModuleIdentity((1,3,6,1,4,1,45,5,49))
if mibBuilder.loadTexts:bayStackNtpMib.setRevisions(('2018-09-27 00:00','2017-07-07 00:00'))
_BsNtpNotifications_ObjectIdentity=ObjectIdentity
bsNtpNotifications=_BsNtpNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,49,0))
_BsNtpObjects_ObjectIdentity=ObjectIdentity
bsNtpObjects=_BsNtpObjects_ObjectIdentity((1,3,6,1,4,1,45,5,49,1))
_BsNtpGlobal_ObjectIdentity=ObjectIdentity
bsNtpGlobal=_BsNtpGlobal_ObjectIdentity((1,3,6,1,4,1,45,5,49,1,1))
class _BsNtpGlobalEnable_Type(TruthValue):defaultValue=2
_BsNtpGlobalEnable_Type.__name__=_E
_BsNtpGlobalEnable_Object=MibScalar
bsNtpGlobalEnable=_BsNtpGlobalEnable_Object((1,3,6,1,4,1,45,5,49,1,1,1),_BsNtpGlobalEnable_Type())
bsNtpGlobalEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:bsNtpGlobalEnable.setStatus(_A)
_BsNtpServerTable_Object=MibTable
bsNtpServerTable=_BsNtpServerTable_Object((1,3,6,1,4,1,45,5,49,1,2))
if mibBuilder.loadTexts:bsNtpServerTable.setStatus(_A)
_BsNtpServerEntry_Object=MibTableRow
bsNtpServerEntry=_BsNtpServerEntry_Object((1,3,6,1,4,1,45,5,49,1,2,1))
bsNtpServerEntry.setIndexNames((0,_G,_H),(0,_G,_I))
if mibBuilder.loadTexts:bsNtpServerEntry.setStatus(_A)
_BsNtpServerAddressType_Type=InetAddressType
_BsNtpServerAddressType_Object=MibTableColumn
bsNtpServerAddressType=_BsNtpServerAddressType_Object((1,3,6,1,4,1,45,5,49,1,2,1,1),_BsNtpServerAddressType_Type())
bsNtpServerAddressType.setMaxAccess(_J)
if mibBuilder.loadTexts:bsNtpServerAddressType.setStatus(_A)
_BsNtpServerAddress_Type=InetAddress
_BsNtpServerAddress_Object=MibTableColumn
bsNtpServerAddress=_BsNtpServerAddress_Object((1,3,6,1,4,1,45,5,49,1,2,1,2),_BsNtpServerAddress_Type())
bsNtpServerAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:bsNtpServerAddress.setStatus(_A)
class _BsNtpServerEnable_Type(TruthValue):defaultValue=1
_BsNtpServerEnable_Type.__name__=_E
_BsNtpServerEnable_Object=MibTableColumn
bsNtpServerEnable=_BsNtpServerEnable_Object((1,3,6,1,4,1,45,5,49,1,2,1,3),_BsNtpServerEnable_Type())
bsNtpServerEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:bsNtpServerEnable.setStatus(_A)
class _BsNtpServerAuthEnable_Type(TruthValue):defaultValue=2
_BsNtpServerAuthEnable_Type.__name__=_E
_BsNtpServerAuthEnable_Object=MibTableColumn
bsNtpServerAuthEnable=_BsNtpServerAuthEnable_Object((1,3,6,1,4,1,45,5,49,1,2,1,4),_BsNtpServerAuthEnable_Type())
bsNtpServerAuthEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:bsNtpServerAuthEnable.setStatus(_A)
class _BsNtpServerKeyId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BsNtpServerKeyId_Type.__name__=_F
_BsNtpServerKeyId_Object=MibTableColumn
bsNtpServerKeyId=_BsNtpServerKeyId_Object((1,3,6,1,4,1,45,5,49,1,2,1,5),_BsNtpServerKeyId_Type())
bsNtpServerKeyId.setMaxAccess(_C)
if mibBuilder.loadTexts:bsNtpServerKeyId.setStatus(_A)
class _BsNtpServerAutokeyEnable_Type(TruthValue):defaultValue=2
_BsNtpServerAutokeyEnable_Type.__name__=_E
_BsNtpServerAutokeyEnable_Object=MibTableColumn
bsNtpServerAutokeyEnable=_BsNtpServerAutokeyEnable_Object((1,3,6,1,4,1,45,5,49,1,2,1,6),_BsNtpServerAutokeyEnable_Type())
bsNtpServerAutokeyEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:bsNtpServerAutokeyEnable.setStatus(_A)
_BsNtpServerVersion_Type=Unsigned32
_BsNtpServerVersion_Object=MibTableColumn
bsNtpServerVersion=_BsNtpServerVersion_Object((1,3,6,1,4,1,45,5,49,1,2,1,7),_BsNtpServerVersion_Type())
bsNtpServerVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:bsNtpServerVersion.setStatus(_A)
_BsNtpServerStratum_Type=Unsigned32
_BsNtpServerStratum_Object=MibTableColumn
bsNtpServerStratum=_BsNtpServerStratum_Object((1,3,6,1,4,1,45,5,49,1,2,1,8),_BsNtpServerStratum_Type())
bsNtpServerStratum.setMaxAccess(_B)
if mibBuilder.loadTexts:bsNtpServerStratum.setStatus(_A)
class _BsNtpServerRootDelay_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BsNtpServerRootDelay_Type.__name__=_D
_BsNtpServerRootDelay_Object=MibTableColumn
bsNtpServerRootDelay=_BsNtpServerRootDelay_Object((1,3,6,1,4,1,45,5,49,1,2,1,9),_BsNtpServerRootDelay_Type())
bsNtpServerRootDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:bsNtpServerRootDelay.setStatus(_A)
_BsNtpServerPrecision_Type=Integer32
_BsNtpServerPrecision_Object=MibTableColumn
bsNtpServerPrecision=_BsNtpServerPrecision_Object((1,3,6,1,4,1,45,5,49,1,2,1,10),_BsNtpServerPrecision_Type())
bsNtpServerPrecision.setMaxAccess(_B)
if mibBuilder.loadTexts:bsNtpServerPrecision.setStatus(_A)
class _BsNtpServerReachable_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_BsNtpServerReachable_Type.__name__=_D
_BsNtpServerReachable_Object=MibTableColumn
bsNtpServerReachable=_BsNtpServerReachable_Object((1,3,6,1,4,1,45,5,49,1,2,1,11),_BsNtpServerReachable_Type())
bsNtpServerReachable.setMaxAccess(_B)
if mibBuilder.loadTexts:bsNtpServerReachable.setStatus(_A)
class _BsNtpServerSynchronized_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_BsNtpServerSynchronized_Type.__name__=_D
_BsNtpServerSynchronized_Object=MibTableColumn
bsNtpServerSynchronized=_BsNtpServerSynchronized_Object((1,3,6,1,4,1,45,5,49,1,2,1,12),_BsNtpServerSynchronized_Type())
bsNtpServerSynchronized.setMaxAccess(_B)
if mibBuilder.loadTexts:bsNtpServerSynchronized.setStatus(_A)
_BsNtpServerPckSent_Type=Counter32
_BsNtpServerPckSent_Object=MibTableColumn
bsNtpServerPckSent=_BsNtpServerPckSent_Object((1,3,6,1,4,1,45,5,49,1,2,1,13),_BsNtpServerPckSent_Type())
bsNtpServerPckSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bsNtpServerPckSent.setStatus(_A)
_BsNtpServerPckProcessed_Type=Counter32
_BsNtpServerPckProcessed_Object=MibTableColumn
bsNtpServerPckProcessed=_BsNtpServerPckProcessed_Object((1,3,6,1,4,1,45,5,49,1,2,1,14),_BsNtpServerPckProcessed_Type())
bsNtpServerPckProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:bsNtpServerPckProcessed.setStatus(_A)
_BsNtpServerPckDiscarded_Type=Counter32
_BsNtpServerPckDiscarded_Object=MibTableColumn
bsNtpServerPckDiscarded=_BsNtpServerPckDiscarded_Object((1,3,6,1,4,1,45,5,49,1,2,1,15),_BsNtpServerPckDiscarded_Type())
bsNtpServerPckDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:bsNtpServerPckDiscarded.setStatus(_A)
_BsNtpServerRowStatus_Type=RowStatus
_BsNtpServerRowStatus_Object=MibTableColumn
bsNtpServerRowStatus=_BsNtpServerRowStatus_Object((1,3,6,1,4,1,45,5,49,1,2,1,16),_BsNtpServerRowStatus_Type())
bsNtpServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bsNtpServerRowStatus.setStatus(_A)
_BsNtpKeyTable_Object=MibTable
bsNtpKeyTable=_BsNtpKeyTable_Object((1,3,6,1,4,1,45,5,49,1,3))
if mibBuilder.loadTexts:bsNtpKeyTable.setStatus(_A)
_BsNtpKeyEntry_Object=MibTableRow
bsNtpKeyEntry=_BsNtpKeyEntry_Object((1,3,6,1,4,1,45,5,49,1,3,1))
bsNtpKeyEntry.setIndexNames((0,_G,_K))
if mibBuilder.loadTexts:bsNtpKeyEntry.setStatus(_A)
class _BsNtpKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BsNtpKeyId_Type.__name__=_F
_BsNtpKeyId_Object=MibTableColumn
bsNtpKeyId=_BsNtpKeyId_Object((1,3,6,1,4,1,45,5,49,1,3,1,1),_BsNtpKeyId_Type())
bsNtpKeyId.setMaxAccess(_B)
if mibBuilder.loadTexts:bsNtpKeyId.setStatus(_A)
class _BsNtpKeyType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('md5',1),('sha1',2)))
_BsNtpKeyType_Type.__name__=_F
_BsNtpKeyType_Object=MibTableColumn
bsNtpKeyType=_BsNtpKeyType_Object((1,3,6,1,4,1,45,5,49,1,3,1,2),_BsNtpKeyType_Type())
bsNtpKeyType.setMaxAccess(_C)
if mibBuilder.loadTexts:bsNtpKeyType.setStatus(_A)
class _BsNtpKeySecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BsNtpKeySecret_Type.__name__=_D
_BsNtpKeySecret_Object=MibTableColumn
bsNtpKeySecret=_BsNtpKeySecret_Object((1,3,6,1,4,1,45,5,49,1,3,1,3),_BsNtpKeySecret_Type())
bsNtpKeySecret.setMaxAccess(_C)
if mibBuilder.loadTexts:bsNtpKeySecret.setStatus(_A)
_BsNtpKeyRowStatus_Type=RowStatus
_BsNtpKeyRowStatus_Object=MibTableColumn
bsNtpKeyRowStatus=_BsNtpKeyRowStatus_Object((1,3,6,1,4,1,45,5,49,1,3,1,4),_BsNtpKeyRowStatus_Type())
bsNtpKeyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bsNtpKeyRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'bayStackNtpMib':bayStackNtpMib,'bsNtpNotifications':bsNtpNotifications,'bsNtpObjects':bsNtpObjects,'bsNtpGlobal':bsNtpGlobal,'bsNtpGlobalEnable':bsNtpGlobalEnable,'bsNtpServerTable':bsNtpServerTable,'bsNtpServerEntry':bsNtpServerEntry,_H:bsNtpServerAddressType,_I:bsNtpServerAddress,'bsNtpServerEnable':bsNtpServerEnable,'bsNtpServerAuthEnable':bsNtpServerAuthEnable,'bsNtpServerKeyId':bsNtpServerKeyId,'bsNtpServerAutokeyEnable':bsNtpServerAutokeyEnable,'bsNtpServerVersion':bsNtpServerVersion,'bsNtpServerStratum':bsNtpServerStratum,'bsNtpServerRootDelay':bsNtpServerRootDelay,'bsNtpServerPrecision':bsNtpServerPrecision,'bsNtpServerReachable':bsNtpServerReachable,'bsNtpServerSynchronized':bsNtpServerSynchronized,'bsNtpServerPckSent':bsNtpServerPckSent,'bsNtpServerPckProcessed':bsNtpServerPckProcessed,'bsNtpServerPckDiscarded':bsNtpServerPckDiscarded,'bsNtpServerRowStatus':bsNtpServerRowStatus,'bsNtpKeyTable':bsNtpKeyTable,'bsNtpKeyEntry':bsNtpKeyEntry,_K:bsNtpKeyId,'bsNtpKeyType':bsNtpKeyType,'bsNtpKeySecret':bsNtpKeySecret,'bsNtpKeyRowStatus':bsNtpKeyRowStatus})