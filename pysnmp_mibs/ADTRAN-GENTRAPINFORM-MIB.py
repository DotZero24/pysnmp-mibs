_P='adTrapHostAddress'
_O='adTrapHostAddressSize'
_N='adTrapHostAddressType'
_M='snmpV3'
_L='snmpV2'
_K='snmpV1'
_J='disabled'
_I='enabled'
_H='adTrapInformHostIP'
_G='not-accessible'
_F='ADTRAN-GENTRAPINFORM-MIB'
_E='read-only'
_D='read-create'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adIdentityShared,adShared=mibBuilder.importSymbols('ADTRAN-MIB','adIdentityShared','adShared')
EntryStatus,=mibBuilder.importSymbols('ADTRAN-TC','EntryStatus')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
adTrapInformID=ModuleIdentity((1,3,6,1,4,1,664,6,10000,101601))
if mibBuilder.loadTexts:adTrapInformID.setRevisions(('2015-11-04 00:00',))
_AdTrapInform_ObjectIdentity=ObjectIdentity
adTrapInform=_AdTrapInform_ObjectIdentity((1,3,6,1,4,1,664,5,16))
_AdTrapInformScalars_ObjectIdentity=ObjectIdentity
adTrapInformScalars=_AdTrapInformScalars_ObjectIdentity((1,3,6,1,4,1,664,5,16,1))
class _AdTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enableTraps',1),('disableTraps',2)))
_AdTrapEnable_Type.__name__=_B
_AdTrapEnable_Object=MibScalar
adTrapEnable=_AdTrapEnable_Object((1,3,6,1,4,1,664,5,16,1,1),_AdTrapEnable_Type())
adTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:adTrapEnable.setStatus(_A)
_AdTrapInformSeqNum_Type=Integer32
_AdTrapInformSeqNum_Object=MibScalar
adTrapInformSeqNum=_AdTrapInformSeqNum_Object((1,3,6,1,4,1,664,5,16,1,2),_AdTrapInformSeqNum_Type())
adTrapInformSeqNum.setMaxAccess(_E)
if mibBuilder.loadTexts:adTrapInformSeqNum.setStatus(_A)
_AdTrapHostEntriesUsed_Type=Integer32
_AdTrapHostEntriesUsed_Object=MibScalar
adTrapHostEntriesUsed=_AdTrapHostEntriesUsed_Object((1,3,6,1,4,1,664,5,16,1,3),_AdTrapHostEntriesUsed_Type())
adTrapHostEntriesUsed.setMaxAccess(_E)
if mibBuilder.loadTexts:adTrapHostEntriesUsed.setStatus(_A)
_AdTrapHostEntryCapacity_Type=Integer32
_AdTrapHostEntryCapacity_Object=MibScalar
adTrapHostEntryCapacity=_AdTrapHostEntryCapacity_Object((1,3,6,1,4,1,664,5,16,1,4),_AdTrapHostEntryCapacity_Type())
adTrapHostEntryCapacity.setMaxAccess(_E)
if mibBuilder.loadTexts:adTrapHostEntryCapacity.setStatus(_A)
_AdTrapInformTables_ObjectIdentity=ObjectIdentity
adTrapInformTables=_AdTrapInformTables_ObjectIdentity((1,3,6,1,4,1,664,5,16,2))
_AdTrapInformHostTable_Object=MibTable
adTrapInformHostTable=_AdTrapInformHostTable_Object((1,3,6,1,4,1,664,5,16,2,1))
if mibBuilder.loadTexts:adTrapInformHostTable.setStatus(_A)
_AdTrapInformHostEntry_Object=MibTableRow
adTrapInformHostEntry=_AdTrapInformHostEntry_Object((1,3,6,1,4,1,664,5,16,2,1,1))
adTrapInformHostEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:adTrapInformHostEntry.setStatus(_A)
_AdTrapInformHostIP_Type=IpAddress
_AdTrapInformHostIP_Object=MibTableColumn
adTrapInformHostIP=_AdTrapInformHostIP_Object((1,3,6,1,4,1,664,5,16,2,1,1,1),_AdTrapInformHostIP_Type())
adTrapInformHostIP.setMaxAccess(_E)
if mibBuilder.loadTexts:adTrapInformHostIP.setStatus(_A)
class _AdTrapInformConfirmation_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_AdTrapInformConfirmation_Type.__name__=_B
_AdTrapInformConfirmation_Object=MibTableColumn
adTrapInformConfirmation=_AdTrapInformConfirmation_Object((1,3,6,1,4,1,664,5,16,2,1,1,2),_AdTrapInformConfirmation_Type())
adTrapInformConfirmation.setMaxAccess(_C)
if mibBuilder.loadTexts:adTrapInformConfirmation.setStatus('deprecated')
class _AdTrapInformSeqNumConfirmed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_AdTrapInformSeqNumConfirmed_Type.__name__=_B
_AdTrapInformSeqNumConfirmed_Object=MibTableColumn
adTrapInformSeqNumConfirmed=_AdTrapInformSeqNumConfirmed_Object((1,3,6,1,4,1,664,5,16,2,1,1,3),_AdTrapInformSeqNumConfirmed_Type())
adTrapInformSeqNumConfirmed.setMaxAccess(_C)
if mibBuilder.loadTexts:adTrapInformSeqNumConfirmed.setStatus(_A)
_AdTrapInformSeqNumRequested_Type=Integer32
_AdTrapInformSeqNumRequested_Object=MibTableColumn
adTrapInformSeqNumRequested=_AdTrapInformSeqNumRequested_Object((1,3,6,1,4,1,664,5,16,2,1,1,4),_AdTrapInformSeqNumRequested_Type())
adTrapInformSeqNumRequested.setMaxAccess(_C)
if mibBuilder.loadTexts:adTrapInformSeqNumRequested.setStatus(_A)
class _AdTrapInformRetryLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_AdTrapInformRetryLimit_Type.__name__=_B
_AdTrapInformRetryLimit_Object=MibTableColumn
adTrapInformRetryLimit=_AdTrapInformRetryLimit_Object((1,3,6,1,4,1,664,5,16,2,1,1,5),_AdTrapInformRetryLimit_Type())
adTrapInformRetryLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:adTrapInformRetryLimit.setStatus(_A)
class _AdTrapInformInitialTimeout_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AdTrapInformInitialTimeout_Type.__name__=_B
_AdTrapInformInitialTimeout_Object=MibTableColumn
adTrapInformInitialTimeout=_AdTrapInformInitialTimeout_Object((1,3,6,1,4,1,664,5,16,2,1,1,6),_AdTrapInformInitialTimeout_Type())
adTrapInformInitialTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:adTrapInformInitialTimeout.setStatus(_A)
_AdTrapInformCache_Type=Integer32
_AdTrapInformCache_Object=MibTableColumn
adTrapInformCache=_AdTrapInformCache_Object((1,3,6,1,4,1,664,5,16,2,1,1,7),_AdTrapInformCache_Type())
adTrapInformCache.setMaxAccess(_E)
if mibBuilder.loadTexts:adTrapInformCache.setStatus(_A)
_AdTrapInformHostStatus_Type=EntryStatus
_AdTrapInformHostStatus_Object=MibTableColumn
adTrapInformHostStatus=_AdTrapInformHostStatus_Object((1,3,6,1,4,1,664,5,16,2,1,1,8),_AdTrapInformHostStatus_Type())
adTrapInformHostStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adTrapInformHostStatus.setStatus(_A)
class _AdTrapInformVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3)))
_AdTrapInformVersion_Type.__name__=_B
_AdTrapInformVersion_Object=MibTableColumn
adTrapInformVersion=_AdTrapInformVersion_Object((1,3,6,1,4,1,664,5,16,2,1,1,9),_AdTrapInformVersion_Type())
adTrapInformVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adTrapInformVersion.setStatus(_A)
_AdTrapHostTable_Object=MibTable
adTrapHostTable=_AdTrapHostTable_Object((1,3,6,1,4,1,664,5,16,2,2))
if mibBuilder.loadTexts:adTrapHostTable.setStatus(_A)
_AdTrapHostEntry_Object=MibTableRow
adTrapHostEntry=_AdTrapHostEntry_Object((1,3,6,1,4,1,664,5,16,2,2,1))
adTrapHostEntry.setIndexNames((0,_F,_N),(0,_F,_O),(0,_F,_P))
if mibBuilder.loadTexts:adTrapHostEntry.setStatus(_A)
_AdTrapHostAddressType_Type=InetAddressType
_AdTrapHostAddressType_Object=MibTableColumn
adTrapHostAddressType=_AdTrapHostAddressType_Object((1,3,6,1,4,1,664,5,16,2,2,1,1),_AdTrapHostAddressType_Type())
adTrapHostAddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:adTrapHostAddressType.setStatus(_A)
class _AdTrapHostAddressSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdTrapHostAddressSize_Type.__name__=_B
_AdTrapHostAddressSize_Object=MibTableColumn
adTrapHostAddressSize=_AdTrapHostAddressSize_Object((1,3,6,1,4,1,664,5,16,2,2,1,2),_AdTrapHostAddressSize_Type())
adTrapHostAddressSize.setMaxAccess(_G)
if mibBuilder.loadTexts:adTrapHostAddressSize.setStatus(_A)
_AdTrapHostAddress_Type=InetAddress
_AdTrapHostAddress_Object=MibTableColumn
adTrapHostAddress=_AdTrapHostAddress_Object((1,3,6,1,4,1,664,5,16,2,2,1,3),_AdTrapHostAddress_Type())
adTrapHostAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:adTrapHostAddress.setStatus(_A)
class _AdTrapHostConfirmation_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_AdTrapHostConfirmation_Type.__name__=_B
_AdTrapHostConfirmation_Object=MibTableColumn
adTrapHostConfirmation=_AdTrapHostConfirmation_Object((1,3,6,1,4,1,664,5,16,2,2,1,4),_AdTrapHostConfirmation_Type())
adTrapHostConfirmation.setMaxAccess(_D)
if mibBuilder.loadTexts:adTrapHostConfirmation.setStatus(_A)
class _AdTrapHostSeqNumConfirmed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_AdTrapHostSeqNumConfirmed_Type.__name__=_B
_AdTrapHostSeqNumConfirmed_Object=MibTableColumn
adTrapHostSeqNumConfirmed=_AdTrapHostSeqNumConfirmed_Object((1,3,6,1,4,1,664,5,16,2,2,1,5),_AdTrapHostSeqNumConfirmed_Type())
adTrapHostSeqNumConfirmed.setMaxAccess(_D)
if mibBuilder.loadTexts:adTrapHostSeqNumConfirmed.setStatus(_A)
_AdTrapHostSeqNumRequested_Type=Integer32
_AdTrapHostSeqNumRequested_Object=MibTableColumn
adTrapHostSeqNumRequested=_AdTrapHostSeqNumRequested_Object((1,3,6,1,4,1,664,5,16,2,2,1,6),_AdTrapHostSeqNumRequested_Type())
adTrapHostSeqNumRequested.setMaxAccess(_D)
if mibBuilder.loadTexts:adTrapHostSeqNumRequested.setStatus(_A)
class _AdTrapHostRetryLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_AdTrapHostRetryLimit_Type.__name__=_B
_AdTrapHostRetryLimit_Object=MibTableColumn
adTrapHostRetryLimit=_AdTrapHostRetryLimit_Object((1,3,6,1,4,1,664,5,16,2,2,1,7),_AdTrapHostRetryLimit_Type())
adTrapHostRetryLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:adTrapHostRetryLimit.setStatus(_A)
class _AdTrapHostInitialTimeout_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AdTrapHostInitialTimeout_Type.__name__=_B
_AdTrapHostInitialTimeout_Object=MibTableColumn
adTrapHostInitialTimeout=_AdTrapHostInitialTimeout_Object((1,3,6,1,4,1,664,5,16,2,2,1,8),_AdTrapHostInitialTimeout_Type())
adTrapHostInitialTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:adTrapHostInitialTimeout.setStatus(_A)
_AdTrapHostCache_Type=Integer32
_AdTrapHostCache_Object=MibTableColumn
adTrapHostCache=_AdTrapHostCache_Object((1,3,6,1,4,1,664,5,16,2,2,1,9),_AdTrapHostCache_Type())
adTrapHostCache.setMaxAccess(_E)
if mibBuilder.loadTexts:adTrapHostCache.setStatus(_A)
class _AdTrapHostVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3)))
_AdTrapHostVersion_Type.__name__=_B
_AdTrapHostVersion_Object=MibTableColumn
adTrapHostVersion=_AdTrapHostVersion_Object((1,3,6,1,4,1,664,5,16,2,2,1,10),_AdTrapHostVersion_Type())
adTrapHostVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:adTrapHostVersion.setStatus(_A)
_AdTrapHostRowStatus_Type=RowStatus
_AdTrapHostRowStatus_Object=MibTableColumn
adTrapHostRowStatus=_AdTrapHostRowStatus_Object((1,3,6,1,4,1,664,5,16,2,2,1,11),_AdTrapHostRowStatus_Type())
adTrapHostRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adTrapHostRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'adTrapInform':adTrapInform,'adTrapInformScalars':adTrapInformScalars,'adTrapEnable':adTrapEnable,'adTrapInformSeqNum':adTrapInformSeqNum,'adTrapHostEntriesUsed':adTrapHostEntriesUsed,'adTrapHostEntryCapacity':adTrapHostEntryCapacity,'adTrapInformTables':adTrapInformTables,'adTrapInformHostTable':adTrapInformHostTable,'adTrapInformHostEntry':adTrapInformHostEntry,_H:adTrapInformHostIP,'adTrapInformConfirmation':adTrapInformConfirmation,'adTrapInformSeqNumConfirmed':adTrapInformSeqNumConfirmed,'adTrapInformSeqNumRequested':adTrapInformSeqNumRequested,'adTrapInformRetryLimit':adTrapInformRetryLimit,'adTrapInformInitialTimeout':adTrapInformInitialTimeout,'adTrapInformCache':adTrapInformCache,'adTrapInformHostStatus':adTrapInformHostStatus,'adTrapInformVersion':adTrapInformVersion,'adTrapHostTable':adTrapHostTable,'adTrapHostEntry':adTrapHostEntry,_N:adTrapHostAddressType,_O:adTrapHostAddressSize,_P:adTrapHostAddress,'adTrapHostConfirmation':adTrapHostConfirmation,'adTrapHostSeqNumConfirmed':adTrapHostSeqNumConfirmed,'adTrapHostSeqNumRequested':adTrapHostSeqNumRequested,'adTrapHostRetryLimit':adTrapHostRetryLimit,'adTrapHostInitialTimeout':adTrapHostInitialTimeout,'adTrapHostCache':adTrapHostCache,'adTrapHostVersion':adTrapHostVersion,'adTrapHostRowStatus':adTrapHostRowStatus,'adTrapInformID':adTrapInformID})