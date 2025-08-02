_u='qtechWlansecurityTrapGroup'
_t='qtechWEPDefaultKeysGroup'
_s='qtechWlansecuritycofigGroup'
_r='qtechWlansecurityWepDecrytErr'
_q='qtechWEPDefaultKeyLength'
_p='qtechWEPDefaultKeyValue'
_o='qtechWlansecurityWepDecrytEnableTrapVar'
_n='qtechWLANEAPAuthenSupport'
_m='qtechACauthenMethodsupport'
_l='qtechWLANsecurityStatus'
_k='qtechWEPAuthenAlgorithm'
_j='qtechRSNpskPassPhrase'
_i='qtechRSNakmmode'
_h='qtechRSNPairwisecipher'
_g='qtechRSNenabled'
_f='qtechWAPIascertificatename'
_e='qtechWAPIlocalcertificatename'
_d='qtechWAPIcacertificatename'
_c='qtechWAPIimportcertificate'
_b='qtechWAPImsrekeyClientoff'
_a='qtechWAPIcertificateformat'
_Z='qtechWAPIasuIpaddress'
_Y='qtechWLANsecry80211i'
_X='qtechWPApskPassPhrase'
_W='qtechWPAakmmode'
_V='qtechWPAPairwisecipher'
_U='qtechWPAenabled'
_T='qtech8021xweplength'
_S='qtechstaticweplength'
_R='qtechWLANsecrymode'
_Q='qtechAPworkmode'
_P='qtechWEPDefaultKeyIndex'
_O='pskor8021x'
_N='ieee8021x'
_M='tkiporaes'
_L='Unsigned32'
_K='qtechWlansecurityDeviceMAC'
_J='wep128'
_I='wep104'
_H='wep40'
_G='TruthValue'
_F='qtechApgWlanId'
_E='QTECH-AC-MGMT-MIB'
_D='Integer32'
_C='read-write'
_B='QTECH-WLAN-SECURITY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechApgWlanId,=mibBuilder.importSymbols(_E,_F)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_G)
qtechWLANsecurityMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,61))
if mibBuilder.loadTexts:qtechWLANsecurityMIB.setRevisions(('2009-10-28 00:00',))
_QtechWLANsecurityTraps_ObjectIdentity=ObjectIdentity
qtechWLANsecurityTraps=_QtechWLANsecurityTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,61,0))
_QtechWLANsecurityMIBObjects_ObjectIdentity=ObjectIdentity
qtechWLANsecurityMIBObjects=_QtechWLANsecurityMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,61,1))
class _QtechAPworkmode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fitap',1),('fatap',2)))
_QtechAPworkmode_Type.__name__=_D
_QtechAPworkmode_Object=MibScalar
qtechAPworkmode=_QtechAPworkmode_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,1),_QtechAPworkmode_Type())
qtechAPworkmode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAPworkmode.setStatus(_A)
_QtechWLANsecurityConfigTable_Object=MibTable
qtechWLANsecurityConfigTable=_QtechWLANsecurityConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2))
if mibBuilder.loadTexts:qtechWLANsecurityConfigTable.setStatus(_A)
_QtechWLANsecurityConfigEntry_Object=MibTableRow
qtechWLANsecurityConfigEntry=_QtechWLANsecurityConfigEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1))
qtechWLANsecurityConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:qtechWLANsecurityConfigEntry.setStatus(_A)
class _QtechWLANsecrymode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('open',1),('staticwep',2),('wep8021x',3),('wpanone',4),('wpapsk',5),('wpa8021x',6),('tsn',7)))
_QtechWLANsecrymode_Type.__name__=_D
_QtechWLANsecrymode_Object=MibTableColumn
qtechWLANsecrymode=_QtechWLANsecrymode_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,1),_QtechWLANsecrymode_Type())
qtechWLANsecrymode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWLANsecrymode.setStatus(_A)
class _Qtechstaticweplength_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3)))
_Qtechstaticweplength_Type.__name__=_D
_Qtechstaticweplength_Object=MibTableColumn
qtechstaticweplength=_Qtechstaticweplength_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,2),_Qtechstaticweplength_Type())
qtechstaticweplength.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechstaticweplength.setStatus(_A)
class _Qtech8021xweplength_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3)))
_Qtech8021xweplength_Type.__name__=_D
_Qtech8021xweplength_Object=MibTableColumn
qtech8021xweplength=_Qtech8021xweplength_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,3),_Qtech8021xweplength_Type())
qtech8021xweplength.setMaxAccess(_C)
if mibBuilder.loadTexts:qtech8021xweplength.setStatus(_A)
class _QtechWPAenabled_Type(TruthValue):defaultValue=2
_QtechWPAenabled_Type.__name__=_G
_QtechWPAenabled_Object=MibTableColumn
qtechWPAenabled=_QtechWPAenabled_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,4),_QtechWPAenabled_Type())
qtechWPAenabled.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWPAenabled.setStatus(_A)
class _QtechWPAPairwisecipher_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tkip',1),('aes',2),(_M,3)))
_QtechWPAPairwisecipher_Type.__name__=_D
_QtechWPAPairwisecipher_Object=MibTableColumn
qtechWPAPairwisecipher=_QtechWPAPairwisecipher_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,5),_QtechWPAPairwisecipher_Type())
qtechWPAPairwisecipher.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWPAPairwisecipher.setStatus(_A)
class _QtechWPAakmmode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('psk',2),(_O,3)))
_QtechWPAakmmode_Type.__name__=_D
_QtechWPAakmmode_Object=MibTableColumn
qtechWPAakmmode=_QtechWPAakmmode_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,6),_QtechWPAakmmode_Type())
qtechWPAakmmode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWPAakmmode.setStatus(_A)
_QtechWPApskPassPhrase_Type=DisplayString
_QtechWPApskPassPhrase_Object=MibTableColumn
qtechWPApskPassPhrase=_QtechWPApskPassPhrase_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,7),_QtechWPApskPassPhrase_Type())
qtechWPApskPassPhrase.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWPApskPassPhrase.setStatus(_A)
class _QtechWLANsecry80211i_Type(TruthValue):defaultValue=1
_QtechWLANsecry80211i_Type.__name__=_G
_QtechWLANsecry80211i_Object=MibTableColumn
qtechWLANsecry80211i=_QtechWLANsecry80211i_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,8),_QtechWLANsecry80211i_Type())
qtechWLANsecry80211i.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWLANsecry80211i.setStatus(_A)
class _QtechWAPIasuIpaddress_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_QtechWAPIasuIpaddress_Type.__name__=_L
_QtechWAPIasuIpaddress_Object=MibTableColumn
qtechWAPIasuIpaddress=_QtechWAPIasuIpaddress_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,9),_QtechWAPIasuIpaddress_Type())
qtechWAPIasuIpaddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWAPIasuIpaddress.setStatus(_A)
class _QtechWAPIcertificateformat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('x509v3',1),('wapigbw',2)))
_QtechWAPIcertificateformat_Type.__name__=_D
_QtechWAPIcertificateformat_Object=MibTableColumn
qtechWAPIcertificateformat=_QtechWAPIcertificateformat_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,10),_QtechWAPIcertificateformat_Type())
qtechWAPIcertificateformat.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWAPIcertificateformat.setStatus(_A)
class _QtechWAPImsrekeyClientoff_Type(TruthValue):defaultValue=2
_QtechWAPImsrekeyClientoff_Type.__name__=_G
_QtechWAPImsrekeyClientoff_Object=MibTableColumn
qtechWAPImsrekeyClientoff=_QtechWAPImsrekeyClientoff_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,11),_QtechWAPImsrekeyClientoff_Type())
qtechWAPImsrekeyClientoff.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWAPImsrekeyClientoff.setStatus(_A)
class _QtechWAPIimportcertificate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ca',1),('local',2),('as',3)))
_QtechWAPIimportcertificate_Type.__name__=_D
_QtechWAPIimportcertificate_Object=MibTableColumn
qtechWAPIimportcertificate=_QtechWAPIimportcertificate_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,12),_QtechWAPIimportcertificate_Type())
qtechWAPIimportcertificate.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWAPIimportcertificate.setStatus(_A)
_QtechWAPIcacertificatename_Type=DisplayString
_QtechWAPIcacertificatename_Object=MibTableColumn
qtechWAPIcacertificatename=_QtechWAPIcacertificatename_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,13),_QtechWAPIcacertificatename_Type())
qtechWAPIcacertificatename.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWAPIcacertificatename.setStatus(_A)
_QtechWAPIlocalcertificatename_Type=DisplayString
_QtechWAPIlocalcertificatename_Object=MibTableColumn
qtechWAPIlocalcertificatename=_QtechWAPIlocalcertificatename_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,14),_QtechWAPIlocalcertificatename_Type())
qtechWAPIlocalcertificatename.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWAPIlocalcertificatename.setStatus(_A)
_QtechWAPIascertificatename_Type=DisplayString
_QtechWAPIascertificatename_Object=MibTableColumn
qtechWAPIascertificatename=_QtechWAPIascertificatename_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,15),_QtechWAPIascertificatename_Type())
qtechWAPIascertificatename.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWAPIascertificatename.setStatus(_A)
_QtechRSNenabled_Type=TruthValue
_QtechRSNenabled_Object=MibTableColumn
qtechRSNenabled=_QtechRSNenabled_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,16),_QtechRSNenabled_Type())
qtechRSNenabled.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRSNenabled.setStatus(_A)
class _QtechRSNPairwisecipher_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tkip',1),('aes',2),(_M,3)))
_QtechRSNPairwisecipher_Type.__name__=_D
_QtechRSNPairwisecipher_Object=MibTableColumn
qtechRSNPairwisecipher=_QtechRSNPairwisecipher_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,17),_QtechRSNPairwisecipher_Type())
qtechRSNPairwisecipher.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRSNPairwisecipher.setStatus(_A)
class _QtechRSNakmmode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('psk',2),(_O,3)))
_QtechRSNakmmode_Type.__name__=_D
_QtechRSNakmmode_Object=MibTableColumn
qtechRSNakmmode=_QtechRSNakmmode_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,18),_QtechRSNakmmode_Type())
qtechRSNakmmode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRSNakmmode.setStatus(_A)
_QtechRSNpskPassPhrase_Type=DisplayString
_QtechRSNpskPassPhrase_Object=MibTableColumn
qtechRSNpskPassPhrase=_QtechRSNpskPassPhrase_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,19),_QtechRSNpskPassPhrase_Type())
qtechRSNpskPassPhrase.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRSNpskPassPhrase.setStatus(_A)
class _QtechWEPAuthenAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('openSystem',1),('sharedKey',2)))
_QtechWEPAuthenAlgorithm_Type.__name__=_D
_QtechWEPAuthenAlgorithm_Object=MibTableColumn
qtechWEPAuthenAlgorithm=_QtechWEPAuthenAlgorithm_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,20),_QtechWEPAuthenAlgorithm_Type())
qtechWEPAuthenAlgorithm.setMaxAccess('read-only')
if mibBuilder.loadTexts:qtechWEPAuthenAlgorithm.setStatus(_A)
_QtechWLANsecurityStatus_Type=RowStatus
_QtechWLANsecurityStatus_Object=MibTableColumn
qtechWLANsecurityStatus=_QtechWLANsecurityStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,21),_QtechWLANsecurityStatus_Type())
qtechWLANsecurityStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWLANsecurityStatus.setStatus(_A)
_QtechACauthenMethodsupport_Type=Integer32
_QtechACauthenMethodsupport_Object=MibTableColumn
qtechACauthenMethodsupport=_QtechACauthenMethodsupport_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,22),_QtechACauthenMethodsupport_Type())
qtechACauthenMethodsupport.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechACauthenMethodsupport.setStatus(_A)
class _QtechWLANEAPAuthenSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('enableEAPAuthentication',0),('disableEAPAuthentication',1),('notSupportingEAPAuthentication',2)))
_QtechWLANEAPAuthenSupport_Type.__name__=_D
_QtechWLANEAPAuthenSupport_Object=MibTableColumn
qtechWLANEAPAuthenSupport=_QtechWLANEAPAuthenSupport_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,2,1,23),_QtechWLANEAPAuthenSupport_Type())
qtechWLANEAPAuthenSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWLANEAPAuthenSupport.setStatus(_A)
_QtechWEPDefaultKeysTable_Object=MibTable
qtechWEPDefaultKeysTable=_QtechWEPDefaultKeysTable_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,3))
if mibBuilder.loadTexts:qtechWEPDefaultKeysTable.setStatus(_A)
_QtechWEPDefaultKeysEntry_Object=MibTableRow
qtechWEPDefaultKeysEntry=_QtechWEPDefaultKeysEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,3,1))
qtechWEPDefaultKeysEntry.setIndexNames((0,_E,_F),(0,_B,_P))
if mibBuilder.loadTexts:qtechWEPDefaultKeysEntry.setStatus(_A)
class _QtechWEPDefaultKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_QtechWEPDefaultKeyIndex_Type.__name__=_D
_QtechWEPDefaultKeyIndex_Object=MibTableColumn
qtechWEPDefaultKeyIndex=_QtechWEPDefaultKeyIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,3,1,1),_QtechWEPDefaultKeyIndex_Type())
qtechWEPDefaultKeyIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:qtechWEPDefaultKeyIndex.setStatus(_A)
_QtechWEPDefaultKeyValue_Type=OctetString
_QtechWEPDefaultKeyValue_Object=MibTableColumn
qtechWEPDefaultKeyValue=_QtechWEPDefaultKeyValue_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,3,1,2),_QtechWEPDefaultKeyValue_Type())
qtechWEPDefaultKeyValue.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWEPDefaultKeyValue.setStatus(_A)
class _QtechWEPDefaultKeyLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3)))
_QtechWEPDefaultKeyLength_Type.__name__=_D
_QtechWEPDefaultKeyLength_Object=MibTableColumn
qtechWEPDefaultKeyLength=_QtechWEPDefaultKeyLength_Object((1,3,6,1,4,1,27514,1,1,10,2,61,1,3,1,3),_QtechWEPDefaultKeyLength_Type())
qtechWEPDefaultKeyLength.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWEPDefaultKeyLength.setStatus(_A)
_QtechWlansecurityMIBConform_ObjectIdentity=ObjectIdentity
qtechWlansecurityMIBConform=_QtechWlansecurityMIBConform_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,61,2))
_QtechWlansecurityMIBCompliances_ObjectIdentity=ObjectIdentity
qtechWlansecurityMIBCompliances=_QtechWlansecurityMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,61,2,1))
_QtechWlansecurityMIBGroups_ObjectIdentity=ObjectIdentity
qtechWlansecurityMIBGroups=_QtechWlansecurityMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,61,2,2))
_QtechWlansecurityTrapvar_ObjectIdentity=ObjectIdentity
qtechWlansecurityTrapvar=_QtechWlansecurityTrapvar_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,61,3))
_QtechWlansecurityWepDecrytEnableTrapVar_Type=Integer32
_QtechWlansecurityWepDecrytEnableTrapVar_Object=MibScalar
qtechWlansecurityWepDecrytEnableTrapVar=_QtechWlansecurityWepDecrytEnableTrapVar_Object((1,3,6,1,4,1,27514,1,1,10,2,61,3,1),_QtechWlansecurityWepDecrytEnableTrapVar_Type())
qtechWlansecurityWepDecrytEnableTrapVar.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlansecurityWepDecrytEnableTrapVar.setStatus(_A)
_QtechWlansecurityDeviceMAC_Type=MacAddress
_QtechWlansecurityDeviceMAC_Object=MibScalar
qtechWlansecurityDeviceMAC=_QtechWlansecurityDeviceMAC_Object((1,3,6,1,4,1,27514,1,1,10,2,61,3,2),_QtechWlansecurityDeviceMAC_Type())
qtechWlansecurityDeviceMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWlansecurityDeviceMAC.setStatus(_A)
qtechWlansecuritycofigGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,61,2,2,1))
qtechWlansecuritycofigGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_K)))
if mibBuilder.loadTexts:qtechWlansecuritycofigGroup.setStatus(_A)
qtechWEPDefaultKeysGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,61,2,2,2))
qtechWEPDefaultKeysGroup.setObjects(*((_B,_p),(_B,_q)))
if mibBuilder.loadTexts:qtechWEPDefaultKeysGroup.setStatus(_A)
qtechWlansecurityWepDecrytErr=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,61,0,1))
qtechWlansecurityWepDecrytErr.setObjects(*((_E,_F),(_B,_K)))
if mibBuilder.loadTexts:qtechWlansecurityWepDecrytErr.setStatus(_A)
qtechWlansecurityTrapGroup=NotificationGroup((1,3,6,1,4,1,27514,1,1,10,2,61,2,2,3))
qtechWlansecurityTrapGroup.setObjects((_B,_r))
if mibBuilder.loadTexts:qtechWlansecurityTrapGroup.setStatus(_A)
qtechWlansecurityMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,61,2,1,1))
qtechWlansecurityMIBCompliance.setObjects(*((_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:qtechWlansecurityMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechWLANsecurityMIB':qtechWLANsecurityMIB,'qtechWLANsecurityTraps':qtechWLANsecurityTraps,_r:qtechWlansecurityWepDecrytErr,'qtechWLANsecurityMIBObjects':qtechWLANsecurityMIBObjects,_Q:qtechAPworkmode,'qtechWLANsecurityConfigTable':qtechWLANsecurityConfigTable,'qtechWLANsecurityConfigEntry':qtechWLANsecurityConfigEntry,_R:qtechWLANsecrymode,_S:qtechstaticweplength,_T:qtech8021xweplength,_U:qtechWPAenabled,_V:qtechWPAPairwisecipher,_W:qtechWPAakmmode,_X:qtechWPApskPassPhrase,_Y:qtechWLANsecry80211i,_Z:qtechWAPIasuIpaddress,_a:qtechWAPIcertificateformat,_b:qtechWAPImsrekeyClientoff,_c:qtechWAPIimportcertificate,_d:qtechWAPIcacertificatename,_e:qtechWAPIlocalcertificatename,_f:qtechWAPIascertificatename,_g:qtechRSNenabled,_h:qtechRSNPairwisecipher,_i:qtechRSNakmmode,_j:qtechRSNpskPassPhrase,_k:qtechWEPAuthenAlgorithm,_l:qtechWLANsecurityStatus,_m:qtechACauthenMethodsupport,_n:qtechWLANEAPAuthenSupport,'qtechWEPDefaultKeysTable':qtechWEPDefaultKeysTable,'qtechWEPDefaultKeysEntry':qtechWEPDefaultKeysEntry,_P:qtechWEPDefaultKeyIndex,_p:qtechWEPDefaultKeyValue,_q:qtechWEPDefaultKeyLength,'qtechWlansecurityMIBConform':qtechWlansecurityMIBConform,'qtechWlansecurityMIBCompliances':qtechWlansecurityMIBCompliances,'qtechWlansecurityMIBCompliance':qtechWlansecurityMIBCompliance,'qtechWlansecurityMIBGroups':qtechWlansecurityMIBGroups,_s:qtechWlansecuritycofigGroup,_t:qtechWEPDefaultKeysGroup,_u:qtechWlansecurityTrapGroup,'qtechWlansecurityTrapvar':qtechWlansecurityTrapvar,_o:qtechWlansecurityWepDecrytEnableTrapVar,_K:qtechWlansecurityDeviceMAC})