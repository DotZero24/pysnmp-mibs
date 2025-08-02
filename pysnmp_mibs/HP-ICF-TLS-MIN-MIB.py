_S='hpicfTlsMinConfigGroup3'
_R='hpicfTlsMinConfigGroup2'
_Q='hpicfTlsMinConfigGroup1'
_P='hpicfTlsMinConfigGroup'
_O='hpicfTlsStrictRfc5424'
_N='hpicfTlsMinCipher'
_M='not-accessible'
_L='TruthValue'
_K='hpicfTlsMinApp'
_J='hpicfTlsMinCipherConfig'
_I='hpicfTlsMinCipherRowStatus'
_H='hpicfTlsMinRowStatus'
_G='hpicfTlsMinCloseSSLSess'
_F='hpicfTlsMinVersion'
_E='read-create'
_D='Integer32'
_C='deprecated'
_B='current'
_A='HP-ICF-TLS-MIN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_L)
hpicfTlsMinMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,112))
if mibBuilder.loadTexts:hpicfTlsMinMIB.setRevisions(('2020-02-24 09:00','2017-05-11 09:00','2017-04-05 09:00','2016-06-22 09:00','2014-10-01 09:00'))
_HpicfTlsMinObjects_ObjectIdentity=ObjectIdentity
hpicfTlsMinObjects=_HpicfTlsMinObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,112,0))
_HpicfTlsMinConfigObjects_ObjectIdentity=ObjectIdentity
hpicfTlsMinConfigObjects=_HpicfTlsMinConfigObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,112,0,1))
_HpicfTlsMinTable_Object=MibTable
hpicfTlsMinTable=_HpicfTlsMinTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,112,0,1,1))
if mibBuilder.loadTexts:hpicfTlsMinTable.setStatus(_B)
_HpicfTlsMinEntry_Object=MibTableRow
hpicfTlsMinEntry=_HpicfTlsMinEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,112,0,1,1,1))
hpicfTlsMinEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:hpicfTlsMinEntry.setStatus(_B)
class _HpicfTlsMinApp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('webSsl',1),('openflow',2),('syslog',3),('tr69',4),('cloud',5),('radsec',6)))
_HpicfTlsMinApp_Type.__name__=_D
_HpicfTlsMinApp_Object=MibTableColumn
hpicfTlsMinApp=_HpicfTlsMinApp_Object((1,3,6,1,4,1,11,2,14,11,5,1,112,0,1,1,1,1),_HpicfTlsMinApp_Type())
hpicfTlsMinApp.setMaxAccess(_M)
if mibBuilder.loadTexts:hpicfTlsMinApp.setStatus(_B)
class _HpicfTlsMinVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tls1dot0',1),('tls1dot1',2),('tls1dot2',3)))
_HpicfTlsMinVersion_Type.__name__=_D
_HpicfTlsMinVersion_Object=MibTableColumn
hpicfTlsMinVersion=_HpicfTlsMinVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,112,0,1,1,1,2),_HpicfTlsMinVersion_Type())
hpicfTlsMinVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfTlsMinVersion.setStatus(_B)
_HpicfTlsMinCloseSSLSess_Type=TruthValue
_HpicfTlsMinCloseSSLSess_Object=MibTableColumn
hpicfTlsMinCloseSSLSess=_HpicfTlsMinCloseSSLSess_Object((1,3,6,1,4,1,11,2,14,11,5,1,112,0,1,1,1,3),_HpicfTlsMinCloseSSLSess_Type())
hpicfTlsMinCloseSSLSess.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfTlsMinCloseSSLSess.setStatus(_B)
_HpicfTlsMinRowStatus_Type=RowStatus
_HpicfTlsMinRowStatus_Object=MibTableColumn
hpicfTlsMinRowStatus=_HpicfTlsMinRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,112,0,1,1,1,4),_HpicfTlsMinRowStatus_Type())
hpicfTlsMinRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfTlsMinRowStatus.setStatus(_B)
class _HpicfTlsStrictRfc5424_Type(TruthValue):defaultValue=2
_HpicfTlsStrictRfc5424_Type.__name__=_L
_HpicfTlsStrictRfc5424_Object=MibTableColumn
hpicfTlsStrictRfc5424=_HpicfTlsStrictRfc5424_Object((1,3,6,1,4,1,11,2,14,11,5,1,112,0,1,1,1,5),_HpicfTlsStrictRfc5424_Type())
hpicfTlsStrictRfc5424.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpicfTlsStrictRfc5424.setStatus(_B)
_HpicfTlsMinCipherTable_Object=MibTable
hpicfTlsMinCipherTable=_HpicfTlsMinCipherTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,112,0,1,2))
if mibBuilder.loadTexts:hpicfTlsMinCipherTable.setStatus(_B)
_HpicfTlsMinCipherEntry_Object=MibTableRow
hpicfTlsMinCipherEntry=_HpicfTlsMinCipherEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,112,0,1,2,1))
hpicfTlsMinCipherEntry.setIndexNames((0,_A,_K),(0,_A,_N))
if mibBuilder.loadTexts:hpicfTlsMinCipherEntry.setStatus(_B)
class _HpicfTlsMinCipher_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36)));namedValues=NamedValues(*(('aes256Sha256',1),('aes256Sha',2),('aes128Sha256',3),('aes128Sha',4),('des3CbcSha',5),('aes256GcmSha384',6),('aes128GcmSha256',7),('ecdhEcdsaAes256GcmSha384',8),('ecdhRsaAaes256GcmSha384',9),('ecdhEcdsaAes128GcmSha256',10),('ecdhRsaAes128GcmSha256',11),('ecdhEcdsaAes256Sha384',12),('ecdhRsaAes256Sha384',13),('ecdhEcdsaAes256Sha',14),('ecdhRsaAes256Sha',15),('ecdhEcdsaAes128Sha256',16),('ecdhRsaAes128Sha256',17),('ecdhEcdsaAes128Sha',18),('ecdhRsaAes128Sha',19),('ecdhEcdsaDesCbc3Sha',20),('ecdhRsaDesCbc3Sha',21),('ecdheEcdsaAes128GcmSha256',22),('ecdheRsaAes128GcmSha256',23),('ecdheEcdsaAes128Sha256',24),('ecdheRsaAes128Sha256',25),('ecdheEcdsaAes128Sha',26),('ecdheRsaAes128Sha',27),('ecdheEcdsaAes256GcmSha384',28),('ecdheRsaAes256GcmSha384',29),('ecdheEcdsaAes256Sha384',30),('ecdheRsaAes256Sha384',31),('ecdheEcdsaAes256Sha',32),('ecdheRsaAes256Sha',33),('ecdheEcdsaDesCbc3Sha',34),('ecdheRsaDesCbc3Sha',35),('all',36)))
_HpicfTlsMinCipher_Type.__name__=_D
_HpicfTlsMinCipher_Object=MibTableColumn
hpicfTlsMinCipher=_HpicfTlsMinCipher_Object((1,3,6,1,4,1,11,2,14,11,5,1,112,0,1,2,1,1),_HpicfTlsMinCipher_Type())
hpicfTlsMinCipher.setMaxAccess(_M)
if mibBuilder.loadTexts:hpicfTlsMinCipher.setStatus(_B)
_HpicfTlsMinCipherRowStatus_Type=RowStatus
_HpicfTlsMinCipherRowStatus_Object=MibTableColumn
hpicfTlsMinCipherRowStatus=_HpicfTlsMinCipherRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,112,0,1,2,1,2),_HpicfTlsMinCipherRowStatus_Type())
hpicfTlsMinCipherRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfTlsMinCipherRowStatus.setStatus(_B)
class _HpicfTlsMinCipherConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enforce',1),('disable',2)))
_HpicfTlsMinCipherConfig_Type.__name__=_D
_HpicfTlsMinCipherConfig_Object=MibTableColumn
hpicfTlsMinCipherConfig=_HpicfTlsMinCipherConfig_Object((1,3,6,1,4,1,11,2,14,11,5,1,112,0,1,2,1,3),_HpicfTlsMinCipherConfig_Type())
hpicfTlsMinCipherConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfTlsMinCipherConfig.setStatus(_B)
_HpicfTlsMinConformance_ObjectIdentity=ObjectIdentity
hpicfTlsMinConformance=_HpicfTlsMinConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,112,1))
_HpicfTlsMinCompliances_ObjectIdentity=ObjectIdentity
hpicfTlsMinCompliances=_HpicfTlsMinCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,112,1,1))
_HpicfTlsMinGroups_ObjectIdentity=ObjectIdentity
hpicfTlsMinGroups=_HpicfTlsMinGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,112,1,2))
hpicfTlsMinConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,112,1,2,1))
hpicfTlsMinConfigGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:hpicfTlsMinConfigGroup.setStatus(_C)
hpicfTlsMinConfigGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,112,1,2,2))
hpicfTlsMinConfigGroup1.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:hpicfTlsMinConfigGroup1.setStatus(_C)
hpicfTlsMinConfigGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,112,1,2,3))
hpicfTlsMinConfigGroup2.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:hpicfTlsMinConfigGroup2.setStatus(_C)
hpicfTlsMinConfigGroup3=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,112,1,2,4))
hpicfTlsMinConfigGroup3.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_O)))
if mibBuilder.loadTexts:hpicfTlsMinConfigGroup3.setStatus(_B)
hpicfTlsMinCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,112,1,1,1))
hpicfTlsMinCompliance1.setObjects((_A,_P))
if mibBuilder.loadTexts:hpicfTlsMinCompliance1.setStatus(_C)
hpicfTlsMinCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,112,1,1,2))
hpicfTlsMinCompliance2.setObjects((_A,_Q))
if mibBuilder.loadTexts:hpicfTlsMinCompliance2.setStatus(_C)
hpicfTlsMinCompliance3=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,112,1,1,3))
hpicfTlsMinCompliance3.setObjects((_A,_R))
if mibBuilder.loadTexts:hpicfTlsMinCompliance3.setStatus(_C)
hpicfTlsMinCompliance4=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,112,1,1,4))
hpicfTlsMinCompliance4.setObjects((_A,_S))
if mibBuilder.loadTexts:hpicfTlsMinCompliance4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfTlsMinMIB':hpicfTlsMinMIB,'hpicfTlsMinObjects':hpicfTlsMinObjects,'hpicfTlsMinConfigObjects':hpicfTlsMinConfigObjects,'hpicfTlsMinTable':hpicfTlsMinTable,'hpicfTlsMinEntry':hpicfTlsMinEntry,_K:hpicfTlsMinApp,_F:hpicfTlsMinVersion,_G:hpicfTlsMinCloseSSLSess,_H:hpicfTlsMinRowStatus,_O:hpicfTlsStrictRfc5424,'hpicfTlsMinCipherTable':hpicfTlsMinCipherTable,'hpicfTlsMinCipherEntry':hpicfTlsMinCipherEntry,_N:hpicfTlsMinCipher,_I:hpicfTlsMinCipherRowStatus,_J:hpicfTlsMinCipherConfig,'hpicfTlsMinConformance':hpicfTlsMinConformance,'hpicfTlsMinCompliances':hpicfTlsMinCompliances,'hpicfTlsMinCompliance1':hpicfTlsMinCompliance1,'hpicfTlsMinCompliance2':hpicfTlsMinCompliance2,'hpicfTlsMinCompliance3':hpicfTlsMinCompliance3,'hpicfTlsMinCompliance4':hpicfTlsMinCompliance4,'hpicfTlsMinGroups':hpicfTlsMinGroups,_P:hpicfTlsMinConfigGroup,_Q:hpicfTlsMinConfigGroup1,_R:hpicfTlsMinConfigGroup2,_S:hpicfTlsMinConfigGroup3})