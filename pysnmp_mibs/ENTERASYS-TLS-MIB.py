_Z='etsysTlsBaseGroup'
_Y='etsysTlsSignatureType'
_X='etsysTlsOperKeyType'
_W='etsysTlsAdminKeyType'
_V='etsysTlsGenerateKeys'
_U='etsysTlsHttpsPort'
_T='etsysTlsKeepOpenTimeout'
_S='etsysTlsMaxHardConnects'
_R='etsysTlsNumHardConnects'
_Q='etsysTlsNumSoftConnects'
_P='etsysTlsEnabled'
_O='rsa3072'
_N='dsa3072'
_M='rsa2048'
_L='dsa2048'
_K='rsa1024'
_J='dsa1024'
_I='rsa768'
_H='dsa768'
_G='rsa512'
_F='dsa512'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='ENTERASYS-TLS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
etsysTlsMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,30))
if mibBuilder.loadTexts:etsysTlsMIB.setRevisions(('2002-11-14 15:34','2002-11-01 21:09'))
_EtsysTlsObjects_ObjectIdentity=ObjectIdentity
etsysTlsObjects=_EtsysTlsObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,30,1))
_EtsysTlsGeneralBranch_ObjectIdentity=ObjectIdentity
etsysTlsGeneralBranch=_EtsysTlsGeneralBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,30,1,1))
class _EtsysTlsEnabled_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enable',1),('disable',2),('reinitialize',3)))
_EtsysTlsEnabled_Type.__name__=_C
_EtsysTlsEnabled_Object=MibScalar
etsysTlsEnabled=_EtsysTlsEnabled_Object((1,3,6,1,4,1,5624,1,2,30,1,1,1),_EtsysTlsEnabled_Type())
etsysTlsEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTlsEnabled.setStatus(_A)
class _EtsysTlsNumSoftConnects_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EtsysTlsNumSoftConnects_Type.__name__=_C
_EtsysTlsNumSoftConnects_Object=MibScalar
etsysTlsNumSoftConnects=_EtsysTlsNumSoftConnects_Object((1,3,6,1,4,1,5624,1,2,30,1,1,2),_EtsysTlsNumSoftConnects_Type())
etsysTlsNumSoftConnects.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTlsNumSoftConnects.setStatus(_A)
class _EtsysTlsNumHardConnects_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EtsysTlsNumHardConnects_Type.__name__=_C
_EtsysTlsNumHardConnects_Object=MibScalar
etsysTlsNumHardConnects=_EtsysTlsNumHardConnects_Object((1,3,6,1,4,1,5624,1,2,30,1,1,3),_EtsysTlsNumHardConnects_Type())
etsysTlsNumHardConnects.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTlsNumHardConnects.setStatus(_A)
class _EtsysTlsMaxHardConnects_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EtsysTlsMaxHardConnects_Type.__name__=_C
_EtsysTlsMaxHardConnects_Object=MibScalar
etsysTlsMaxHardConnects=_EtsysTlsMaxHardConnects_Object((1,3,6,1,4,1,5624,1,2,30,1,1,4),_EtsysTlsMaxHardConnects_Type())
etsysTlsMaxHardConnects.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysTlsMaxHardConnects.setStatus(_A)
_EtsysTlsNetworkBranch_ObjectIdentity=ObjectIdentity
etsysTlsNetworkBranch=_EtsysTlsNetworkBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,30,1,2))
class _EtsysTlsKeepOpenTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EtsysTlsKeepOpenTimeout_Type.__name__=_C
_EtsysTlsKeepOpenTimeout_Object=MibScalar
etsysTlsKeepOpenTimeout=_EtsysTlsKeepOpenTimeout_Object((1,3,6,1,4,1,5624,1,2,30,1,2,1),_EtsysTlsKeepOpenTimeout_Type())
etsysTlsKeepOpenTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTlsKeepOpenTimeout.setStatus(_A)
class _EtsysTlsHttpsPort_Type(Integer32):defaultValue=443;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EtsysTlsHttpsPort_Type.__name__=_C
_EtsysTlsHttpsPort_Object=MibScalar
etsysTlsHttpsPort=_EtsysTlsHttpsPort_Object((1,3,6,1,4,1,5624,1,2,30,1,2,2),_EtsysTlsHttpsPort_Type())
etsysTlsHttpsPort.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTlsHttpsPort.setStatus(_A)
_EtsysTlsServerKeyBranch_ObjectIdentity=ObjectIdentity
etsysTlsServerKeyBranch=_EtsysTlsServerKeyBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,30,1,3))
class _EtsysTlsGenerateKeys_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notInitiated',1),('completed',2),('failed',3),('generate',4),('completedPending',5)))
_EtsysTlsGenerateKeys_Type.__name__=_C
_EtsysTlsGenerateKeys_Object=MibScalar
etsysTlsGenerateKeys=_EtsysTlsGenerateKeys_Object((1,3,6,1,4,1,5624,1,2,30,1,3,1),_EtsysTlsGenerateKeys_Type())
etsysTlsGenerateKeys.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTlsGenerateKeys.setStatus(_A)
class _EtsysTlsAdminKeyType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7),(_M,8),(_N,9),(_O,10)))
_EtsysTlsAdminKeyType_Type.__name__=_C
_EtsysTlsAdminKeyType_Object=MibScalar
etsysTlsAdminKeyType=_EtsysTlsAdminKeyType_Object((1,3,6,1,4,1,5624,1,2,30,1,3,2),_EtsysTlsAdminKeyType_Type())
etsysTlsAdminKeyType.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTlsAdminKeyType.setStatus(_A)
class _EtsysTlsOperKeyType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,99)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7),(_M,8),(_N,9),(_O,10),('none',99)))
_EtsysTlsOperKeyType_Type.__name__=_C
_EtsysTlsOperKeyType_Object=MibScalar
etsysTlsOperKeyType=_EtsysTlsOperKeyType_Object((1,3,6,1,4,1,5624,1,2,30,1,3,3),_EtsysTlsOperKeyType_Type())
etsysTlsOperKeyType.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysTlsOperKeyType.setStatus(_A)
class _EtsysTlsSignatureType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('dhAnon',1),('dsaSha1',2),('dsaSha',3),('rsaSha1',4),('rsaMd2',5),('rsaMd5',6)))
_EtsysTlsSignatureType_Type.__name__=_C
_EtsysTlsSignatureType_Object=MibScalar
etsysTlsSignatureType=_EtsysTlsSignatureType_Object((1,3,6,1,4,1,5624,1,2,30,1,3,4),_EtsysTlsSignatureType_Type())
etsysTlsSignatureType.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTlsSignatureType.setStatus(_A)
_EtsysTlsConformance_ObjectIdentity=ObjectIdentity
etsysTlsConformance=_EtsysTlsConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,30,2))
_EtsysTlsGroups_ObjectIdentity=ObjectIdentity
etsysTlsGroups=_EtsysTlsGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,30,2,1))
_EtsysTlsCompliances_ObjectIdentity=ObjectIdentity
etsysTlsCompliances=_EtsysTlsCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,30,2,2))
etsysTlsBaseGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,30,2,1,1))
etsysTlsBaseGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:etsysTlsBaseGroup.setStatus(_A)
etsysTlsCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,30,2,2,1))
etsysTlsCompliance.setObjects((_B,_Z))
if mibBuilder.loadTexts:etsysTlsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysTlsMIB':etsysTlsMIB,'etsysTlsObjects':etsysTlsObjects,'etsysTlsGeneralBranch':etsysTlsGeneralBranch,_P:etsysTlsEnabled,_Q:etsysTlsNumSoftConnects,_R:etsysTlsNumHardConnects,_S:etsysTlsMaxHardConnects,'etsysTlsNetworkBranch':etsysTlsNetworkBranch,_T:etsysTlsKeepOpenTimeout,_U:etsysTlsHttpsPort,'etsysTlsServerKeyBranch':etsysTlsServerKeyBranch,_V:etsysTlsGenerateKeys,_W:etsysTlsAdminKeyType,_X:etsysTlsOperKeyType,_Y:etsysTlsSignatureType,'etsysTlsConformance':etsysTlsConformance,'etsysTlsGroups':etsysTlsGroups,_Z:etsysTlsBaseGroup,'etsysTlsCompliances':etsysTlsCompliances,'etsysTlsCompliance':etsysTlsCompliance})