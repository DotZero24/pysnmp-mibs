_l='cieMIBGroup'
_k='cieTestConnEntryStatus'
_j='cieTestConnEntryOwner'
_i='cieTestConnCryptoMapTagNumber'
_h='cieTestConnCryptoMapName'
_g='cieTestConnTrapOnCompletion'
_f='cieAlgorithmType'
_e='cieLocalTimeEstablished'
_d='ciePktsDropped'
_c='ciePktsDecrypted'
_b='ciePktsEncrypted'
_a='cieConnStatus'
_Z='cieUnprotectedAddr'
_Y='cieProtectedAddr'
_X='cieNumberOfConnections'
_W='cieEsaMode'
_V='cieEsaAuthenticated'
_U='cieEsaTampered'
_T='cieEnginePublicKey'
_S='cieEngineCardIndex'
_R='cieNumberOfCryptoEngines'
_Q='cieEncryptionKeyTimeout'
_P='cieConfiguredAlgorithms'
_O='cieTestConnSerialNumber'
_N='not-accessible'
_M='cieConnIndex'
_L='TruthValue'
_K='RowStatus'
_J='cieTestConnSessionStatus'
_I='cieTestConnUnprotectedAddr'
_H='cieTestConnProtectedAddr'
_G='OctetString'
_F='cieEngineID'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='CISCO-IP-ENCRYPTION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
OwnerString,=mibBuilder.importSymbols('IF-MIB','OwnerString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress',_K,'TextualConvention','TimeStamp',_L)
ciscoIpEncryptionMIB=ModuleIdentity((1,3,6,1,4,1,9,9,52))
_CiscoIpEncryptionMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIpEncryptionMIBObjects=_CiscoIpEncryptionMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,52,1))
_CieConfig_ObjectIdentity=ObjectIdentity
cieConfig=_CieConfig_ObjectIdentity((1,3,6,1,4,1,9,9,52,1,1))
class _CieConfiguredAlgorithms_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_CieConfiguredAlgorithms_Type.__name__=_G
_CieConfiguredAlgorithms_Object=MibScalar
cieConfiguredAlgorithms=_CieConfiguredAlgorithms_Object((1,3,6,1,4,1,9,9,52,1,1,1),_CieConfiguredAlgorithms_Type())
cieConfiguredAlgorithms.setMaxAccess(_C)
if mibBuilder.loadTexts:cieConfiguredAlgorithms.setStatus(_A)
_CieEncryptionKeyTimeout_Type=Integer32
_CieEncryptionKeyTimeout_Object=MibScalar
cieEncryptionKeyTimeout=_CieEncryptionKeyTimeout_Object((1,3,6,1,4,1,9,9,52,1,1,2),_CieEncryptionKeyTimeout_Type())
cieEncryptionKeyTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cieEncryptionKeyTimeout.setStatus(_A)
if mibBuilder.loadTexts:cieEncryptionKeyTimeout.setUnits('minutes')
_CieNumberOfCryptoEngines_Type=Gauge32
_CieNumberOfCryptoEngines_Object=MibScalar
cieNumberOfCryptoEngines=_CieNumberOfCryptoEngines_Object((1,3,6,1,4,1,9,9,52,1,1,3),_CieNumberOfCryptoEngines_Type())
cieNumberOfCryptoEngines.setMaxAccess(_C)
if mibBuilder.loadTexts:cieNumberOfCryptoEngines.setStatus(_A)
_CieEngineStatus_ObjectIdentity=ObjectIdentity
cieEngineStatus=_CieEngineStatus_ObjectIdentity((1,3,6,1,4,1,9,9,52,1,2))
_CieEngineStatusTable_Object=MibTable
cieEngineStatusTable=_CieEngineStatusTable_Object((1,3,6,1,4,1,9,9,52,1,2,1))
if mibBuilder.loadTexts:cieEngineStatusTable.setStatus(_A)
_CieEngineStatusEntry_Object=MibTableRow
cieEngineStatusEntry=_CieEngineStatusEntry_Object((1,3,6,1,4,1,9,9,52,1,2,1,1))
cieEngineStatusEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cieEngineStatusEntry.setStatus(_A)
class _CieEngineID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CieEngineID_Type.__name__=_D
_CieEngineID_Object=MibTableColumn
cieEngineID=_CieEngineID_Object((1,3,6,1,4,1,9,9,52,1,2,1,1,1),_CieEngineID_Type())
cieEngineID.setMaxAccess(_C)
if mibBuilder.loadTexts:cieEngineID.setStatus(_A)
_CieEngineCardIndex_Type=Integer32
_CieEngineCardIndex_Object=MibTableColumn
cieEngineCardIndex=_CieEngineCardIndex_Object((1,3,6,1,4,1,9,9,52,1,2,1,1,2),_CieEngineCardIndex_Type())
cieEngineCardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cieEngineCardIndex.setStatus(_A)
class _CieEnginePublicKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CieEnginePublicKey_Type.__name__=_G
_CieEnginePublicKey_Object=MibTableColumn
cieEnginePublicKey=_CieEnginePublicKey_Object((1,3,6,1,4,1,9,9,52,1,2,1,1,3),_CieEnginePublicKey_Type())
cieEnginePublicKey.setMaxAccess(_C)
if mibBuilder.loadTexts:cieEnginePublicKey.setStatus(_A)
_CieEsaTampered_Type=TruthValue
_CieEsaTampered_Object=MibTableColumn
cieEsaTampered=_CieEsaTampered_Object((1,3,6,1,4,1,9,9,52,1,2,1,1,4),_CieEsaTampered_Type())
cieEsaTampered.setMaxAccess(_C)
if mibBuilder.loadTexts:cieEsaTampered.setStatus(_A)
_CieEsaAuthenticated_Type=TruthValue
_CieEsaAuthenticated_Object=MibTableColumn
cieEsaAuthenticated=_CieEsaAuthenticated_Object((1,3,6,1,4,1,9,9,52,1,2,1,1,5),_CieEsaAuthenticated_Type())
cieEsaAuthenticated.setMaxAccess(_C)
if mibBuilder.loadTexts:cieEsaAuthenticated.setStatus(_A)
class _CieEsaMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enableActive',1),('boot',2),('error',3)))
_CieEsaMode_Type.__name__=_D
_CieEsaMode_Object=MibTableColumn
cieEsaMode=_CieEsaMode_Object((1,3,6,1,4,1,9,9,52,1,2,1,1,6),_CieEsaMode_Type())
cieEsaMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cieEsaMode.setStatus(_A)
_CieConnections_ObjectIdentity=ObjectIdentity
cieConnections=_CieConnections_ObjectIdentity((1,3,6,1,4,1,9,9,52,1,3))
_CieNumberOfConnections_Type=Gauge32
_CieNumberOfConnections_Object=MibScalar
cieNumberOfConnections=_CieNumberOfConnections_Object((1,3,6,1,4,1,9,9,52,1,3,1),_CieNumberOfConnections_Type())
cieNumberOfConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:cieNumberOfConnections.setStatus(_A)
_CieConnTable_Object=MibTable
cieConnTable=_CieConnTable_Object((1,3,6,1,4,1,9,9,52,1,3,2))
if mibBuilder.loadTexts:cieConnTable.setStatus(_A)
_CieConnEntry_Object=MibTableRow
cieConnEntry=_CieConnEntry_Object((1,3,6,1,4,1,9,9,52,1,3,2,1))
cieConnEntry.setIndexNames((0,_B,_F),(0,_B,_M))
if mibBuilder.loadTexts:cieConnEntry.setStatus(_A)
class _CieConnIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CieConnIndex_Type.__name__=_D
_CieConnIndex_Object=MibTableColumn
cieConnIndex=_CieConnIndex_Object((1,3,6,1,4,1,9,9,52,1,3,2,1,1),_CieConnIndex_Type())
cieConnIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:cieConnIndex.setStatus(_A)
_CieProtectedAddr_Type=IpAddress
_CieProtectedAddr_Object=MibTableColumn
cieProtectedAddr=_CieProtectedAddr_Object((1,3,6,1,4,1,9,9,52,1,3,2,1,2),_CieProtectedAddr_Type())
cieProtectedAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cieProtectedAddr.setStatus(_A)
_CieUnprotectedAddr_Type=IpAddress
_CieUnprotectedAddr_Object=MibTableColumn
cieUnprotectedAddr=_CieUnprotectedAddr_Object((1,3,6,1,4,1,9,9,52,1,3,2,1,3),_CieUnprotectedAddr_Type())
cieUnprotectedAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cieUnprotectedAddr.setStatus(_A)
class _CieConnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('pendingConnection',1),('openConnection',2),('exchangeKeys',3),('badConnection',4)))
_CieConnStatus_Type.__name__=_D
_CieConnStatus_Object=MibTableColumn
cieConnStatus=_CieConnStatus_Object((1,3,6,1,4,1,9,9,52,1,3,2,1,4),_CieConnStatus_Type())
cieConnStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cieConnStatus.setStatus(_A)
_CiePktsEncrypted_Type=Counter32
_CiePktsEncrypted_Object=MibTableColumn
ciePktsEncrypted=_CiePktsEncrypted_Object((1,3,6,1,4,1,9,9,52,1,3,2,1,5),_CiePktsEncrypted_Type())
ciePktsEncrypted.setMaxAccess(_C)
if mibBuilder.loadTexts:ciePktsEncrypted.setStatus(_A)
_CiePktsDecrypted_Type=Counter32
_CiePktsDecrypted_Object=MibTableColumn
ciePktsDecrypted=_CiePktsDecrypted_Object((1,3,6,1,4,1,9,9,52,1,3,2,1,6),_CiePktsDecrypted_Type())
ciePktsDecrypted.setMaxAccess(_C)
if mibBuilder.loadTexts:ciePktsDecrypted.setStatus(_A)
_CiePktsDropped_Type=Counter32
_CiePktsDropped_Object=MibTableColumn
ciePktsDropped=_CiePktsDropped_Object((1,3,6,1,4,1,9,9,52,1,3,2,1,7),_CiePktsDropped_Type())
ciePktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:ciePktsDropped.setStatus(_A)
_CieLocalTimeEstablished_Type=TimeStamp
_CieLocalTimeEstablished_Object=MibTableColumn
cieLocalTimeEstablished=_CieLocalTimeEstablished_Object((1,3,6,1,4,1,9,9,52,1,3,2,1,8),_CieLocalTimeEstablished_Type())
cieLocalTimeEstablished.setMaxAccess(_C)
if mibBuilder.loadTexts:cieLocalTimeEstablished.setStatus(_A)
class _CieAlgorithmType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('des56bitCfb64',1),('des56bitCfb8',2),('des40bitCfb64',3),('des40bitdesCfb8',4)))
_CieAlgorithmType_Type.__name__=_D
_CieAlgorithmType_Object=MibTableColumn
cieAlgorithmType=_CieAlgorithmType_Object((1,3,6,1,4,1,9,9,52,1,3,2,1,9),_CieAlgorithmType_Type())
cieAlgorithmType.setMaxAccess(_C)
if mibBuilder.loadTexts:cieAlgorithmType.setStatus(_A)
_CieTestConnection_ObjectIdentity=ObjectIdentity
cieTestConnection=_CieTestConnection_ObjectIdentity((1,3,6,1,4,1,9,9,52,1,4))
_CieTestConnTable_Object=MibTable
cieTestConnTable=_CieTestConnTable_Object((1,3,6,1,4,1,9,9,52,1,4,1))
if mibBuilder.loadTexts:cieTestConnTable.setStatus(_A)
_CieTestConnEntry_Object=MibTableRow
cieTestConnEntry=_CieTestConnEntry_Object((1,3,6,1,4,1,9,9,52,1,4,1,1))
cieTestConnEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:cieTestConnEntry.setStatus(_A)
class _CieTestConnSerialNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CieTestConnSerialNumber_Type.__name__=_D
_CieTestConnSerialNumber_Object=MibTableColumn
cieTestConnSerialNumber=_CieTestConnSerialNumber_Object((1,3,6,1,4,1,9,9,52,1,4,1,1,1),_CieTestConnSerialNumber_Type())
cieTestConnSerialNumber.setMaxAccess(_N)
if mibBuilder.loadTexts:cieTestConnSerialNumber.setStatus(_A)
_CieTestConnProtectedAddr_Type=IpAddress
_CieTestConnProtectedAddr_Object=MibTableColumn
cieTestConnProtectedAddr=_CieTestConnProtectedAddr_Object((1,3,6,1,4,1,9,9,52,1,4,1,1,2),_CieTestConnProtectedAddr_Type())
cieTestConnProtectedAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cieTestConnProtectedAddr.setStatus(_A)
_CieTestConnUnprotectedAddr_Type=IpAddress
_CieTestConnUnprotectedAddr_Object=MibTableColumn
cieTestConnUnprotectedAddr=_CieTestConnUnprotectedAddr_Object((1,3,6,1,4,1,9,9,52,1,4,1,1,3),_CieTestConnUnprotectedAddr_Type())
cieTestConnUnprotectedAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cieTestConnUnprotectedAddr.setStatus(_A)
class _CieTestConnTrapOnCompletion_Type(TruthValue):defaultValue=2
_CieTestConnTrapOnCompletion_Type.__name__=_L
_CieTestConnTrapOnCompletion_Object=MibTableColumn
cieTestConnTrapOnCompletion=_CieTestConnTrapOnCompletion_Object((1,3,6,1,4,1,9,9,52,1,4,1,1,4),_CieTestConnTrapOnCompletion_Type())
cieTestConnTrapOnCompletion.setMaxAccess(_E)
if mibBuilder.loadTexts:cieTestConnTrapOnCompletion.setStatus(_A)
_CieTestConnCryptoMapName_Type=DisplayString
_CieTestConnCryptoMapName_Object=MibTableColumn
cieTestConnCryptoMapName=_CieTestConnCryptoMapName_Object((1,3,6,1,4,1,9,9,52,1,4,1,1,5),_CieTestConnCryptoMapName_Type())
cieTestConnCryptoMapName.setMaxAccess(_E)
if mibBuilder.loadTexts:cieTestConnCryptoMapName.setStatus(_A)
class _CieTestConnCryptoMapTagNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CieTestConnCryptoMapTagNumber_Type.__name__=_D
_CieTestConnCryptoMapTagNumber_Object=MibTableColumn
cieTestConnCryptoMapTagNumber=_CieTestConnCryptoMapTagNumber_Object((1,3,6,1,4,1,9,9,52,1,4,1,1,6),_CieTestConnCryptoMapTagNumber_Type())
cieTestConnCryptoMapTagNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:cieTestConnCryptoMapTagNumber.setStatus(_A)
class _CieTestConnSessionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('inProgress',1),('fail',2),('success',3),('badCryptoMapName',4)))
_CieTestConnSessionStatus_Type.__name__=_D
_CieTestConnSessionStatus_Object=MibTableColumn
cieTestConnSessionStatus=_CieTestConnSessionStatus_Object((1,3,6,1,4,1,9,9,52,1,4,1,1,7),_CieTestConnSessionStatus_Type())
cieTestConnSessionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cieTestConnSessionStatus.setStatus(_A)
_CieTestConnEntryOwner_Type=OwnerString
_CieTestConnEntryOwner_Object=MibTableColumn
cieTestConnEntryOwner=_CieTestConnEntryOwner_Object((1,3,6,1,4,1,9,9,52,1,4,1,1,8),_CieTestConnEntryOwner_Type())
cieTestConnEntryOwner.setMaxAccess(_E)
if mibBuilder.loadTexts:cieTestConnEntryOwner.setStatus(_A)
class _CieTestConnEntryStatus_Type(RowStatus):defaultValue=4
_CieTestConnEntryStatus_Type.__name__=_K
_CieTestConnEntryStatus_Object=MibTableColumn
cieTestConnEntryStatus=_CieTestConnEntryStatus_Object((1,3,6,1,4,1,9,9,52,1,4,1,1,9),_CieTestConnEntryStatus_Type())
cieTestConnEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cieTestConnEntryStatus.setStatus(_A)
_CieMIBTrapPrefix_ObjectIdentity=ObjectIdentity
cieMIBTrapPrefix=_CieMIBTrapPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,52,2))
_CieMIBTraps_ObjectIdentity=ObjectIdentity
cieMIBTraps=_CieMIBTraps_ObjectIdentity((1,3,6,1,4,1,9,9,52,2,0))
_CieMIBConformance_ObjectIdentity=ObjectIdentity
cieMIBConformance=_CieMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,52,3))
_CieMIBCompliances_ObjectIdentity=ObjectIdentity
cieMIBCompliances=_CieMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,52,3,1))
_CieMIBGroups_ObjectIdentity=ObjectIdentity
cieMIBGroups=_CieMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,52,3,2))
cieMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,52,3,2,1))
cieMIBGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_F),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_H),(_B,_I),(_B,_g),(_B,_h),(_B,_i),(_B,_J),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:cieMIBGroup.setStatus(_A)
cieTestCompletion=NotificationType((1,3,6,1,4,1,9,9,52,2,0,1))
cieTestCompletion.setObjects(*((_B,_J),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:cieTestCompletion.setStatus(_A)
cieMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,52,3,1,1))
cieMIBCompliance.setObjects((_B,_l))
if mibBuilder.loadTexts:cieMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoIpEncryptionMIB':ciscoIpEncryptionMIB,'ciscoIpEncryptionMIBObjects':ciscoIpEncryptionMIBObjects,'cieConfig':cieConfig,_P:cieConfiguredAlgorithms,_Q:cieEncryptionKeyTimeout,_R:cieNumberOfCryptoEngines,'cieEngineStatus':cieEngineStatus,'cieEngineStatusTable':cieEngineStatusTable,'cieEngineStatusEntry':cieEngineStatusEntry,_F:cieEngineID,_S:cieEngineCardIndex,_T:cieEnginePublicKey,_U:cieEsaTampered,_V:cieEsaAuthenticated,_W:cieEsaMode,'cieConnections':cieConnections,_X:cieNumberOfConnections,'cieConnTable':cieConnTable,'cieConnEntry':cieConnEntry,_M:cieConnIndex,_Y:cieProtectedAddr,_Z:cieUnprotectedAddr,_a:cieConnStatus,_b:ciePktsEncrypted,_c:ciePktsDecrypted,_d:ciePktsDropped,_e:cieLocalTimeEstablished,_f:cieAlgorithmType,'cieTestConnection':cieTestConnection,'cieTestConnTable':cieTestConnTable,'cieTestConnEntry':cieTestConnEntry,_O:cieTestConnSerialNumber,_H:cieTestConnProtectedAddr,_I:cieTestConnUnprotectedAddr,_g:cieTestConnTrapOnCompletion,_h:cieTestConnCryptoMapName,_i:cieTestConnCryptoMapTagNumber,_J:cieTestConnSessionStatus,_j:cieTestConnEntryOwner,_k:cieTestConnEntryStatus,'cieMIBTrapPrefix':cieMIBTrapPrefix,'cieMIBTraps':cieMIBTraps,'cieTestCompletion':cieTestCompletion,'cieMIBConformance':cieMIBConformance,'cieMIBCompliances':cieMIBCompliances,'cieMIBCompliance':cieMIBCompliance,'cieMIBGroups':cieMIBGroups,_l:cieMIBGroup})