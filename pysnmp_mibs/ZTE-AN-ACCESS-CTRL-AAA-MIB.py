_Q='zxAnAaaAccountUserPrivilege'
_P='zxAnAaaAuthorSessionType'
_O='zxAnAaaAuthenLoginMode'
_N='tacacsPlus'
_M='telnet'
_L='zxAnAaaAuthenSessionType'
_K='ZxAnAaaAuthorMethodPriority'
_J='disabled'
_I='enabled'
_H='not-accessible'
_G='ZTE-AN-ACCESS-CTRL-AAA-MIB'
_F='ZxAnAaaAuthenMethodPriority'
_E='DisplayString'
_D='read-write'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
zxAn,=mibBuilder.importSymbols('ZTE-AN-TC-MIB','zxAn')
zxAnAccessCtrlAaaMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,90))
if mibBuilder.loadTexts:zxAnAccessCtrlAaaMib.setRevisions(('2012-11-07 10:00',))
class ZxAnAaaAuthenMethodPriority(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
class ZxAnAaaAuthorMethodPriority(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_ZxAnAaaAuthenticationObjects_ObjectIdentity=ObjectIdentity
zxAnAaaAuthenticationObjects=_ZxAnAaaAuthenticationObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,90,2))
_ZxAnAaaAuthenGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnAaaAuthenGlobalObjects=_ZxAnAaaAuthenGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,90,2,1))
class _ZxAnAaaAuthenLocalPriority_Type(ZxAnAaaAuthenMethodPriority):defaultValue=0
_ZxAnAaaAuthenLocalPriority_Type.__name__=_F
_ZxAnAaaAuthenLocalPriority_Object=MibScalar
zxAnAaaAuthenLocalPriority=_ZxAnAaaAuthenLocalPriority_Object((1,3,6,1,4,1,3902,1015,90,2,1,1),_ZxAnAaaAuthenLocalPriority_Type())
zxAnAaaAuthenLocalPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAaaAuthenLocalPriority.setStatus(_A)
class _ZxAnAaaAuthenTacacsplusPriority_Type(ZxAnAaaAuthenMethodPriority):defaultValue=0
_ZxAnAaaAuthenTacacsplusPriority_Type.__name__=_F
_ZxAnAaaAuthenTacacsplusPriority_Object=MibScalar
zxAnAaaAuthenTacacsplusPriority=_ZxAnAaaAuthenTacacsplusPriority_Object((1,3,6,1,4,1,3902,1015,90,2,1,2),_ZxAnAaaAuthenTacacsplusPriority_Type())
zxAnAaaAuthenTacacsplusPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAaaAuthenTacacsplusPriority.setStatus(_A)
class _ZxAnAaaAuthenNoAuthenMethodEn_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_ZxAnAaaAuthenNoAuthenMethodEn_Type.__name__=_C
_ZxAnAaaAuthenNoAuthenMethodEn_Object=MibScalar
zxAnAaaAuthenNoAuthenMethodEn=_ZxAnAaaAuthenNoAuthenMethodEn_Object((1,3,6,1,4,1,3902,1015,90,2,1,3),_ZxAnAaaAuthenNoAuthenMethodEn_Type())
zxAnAaaAuthenNoAuthenMethodEn.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAaaAuthenNoAuthenMethodEn.setStatus(_A)
class _ZxAnAaaAuthenTacacsplusGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnAaaAuthenTacacsplusGroupName_Type.__name__=_E
_ZxAnAaaAuthenTacacsplusGroupName_Object=MibScalar
zxAnAaaAuthenTacacsplusGroupName=_ZxAnAaaAuthenTacacsplusGroupName_Object((1,3,6,1,4,1,3902,1015,90,2,1,4),_ZxAnAaaAuthenTacacsplusGroupName_Type())
zxAnAaaAuthenTacacsplusGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAaaAuthenTacacsplusGroupName.setStatus(_A)
_ZxAnAaaAuthenticationSession_ObjectIdentity=ObjectIdentity
zxAnAaaAuthenticationSession=_ZxAnAaaAuthenticationSession_ObjectIdentity((1,3,6,1,4,1,3902,1015,90,2,2))
_ZxAnAaaAuthenSessionTable_Object=MibTable
zxAnAaaAuthenSessionTable=_ZxAnAaaAuthenSessionTable_Object((1,3,6,1,4,1,3902,1015,90,2,2,2))
if mibBuilder.loadTexts:zxAnAaaAuthenSessionTable.setStatus(_A)
_ZxAnAaaAuthenSessionEntry_Object=MibTableRow
zxAnAaaAuthenSessionEntry=_ZxAnAaaAuthenSessionEntry_Object((1,3,6,1,4,1,3902,1015,90,2,2,2,1))
zxAnAaaAuthenSessionEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:zxAnAaaAuthenSessionEntry.setStatus(_A)
class _ZxAnAaaAuthenSessionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),('ssh',2)))
_ZxAnAaaAuthenSessionType_Type.__name__=_C
_ZxAnAaaAuthenSessionType_Object=MibTableColumn
zxAnAaaAuthenSessionType=_ZxAnAaaAuthenSessionType_Object((1,3,6,1,4,1,3902,1015,90,2,2,2,1,1),_ZxAnAaaAuthenSessionType_Type())
zxAnAaaAuthenSessionType.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnAaaAuthenSessionType.setStatus(_A)
class _ZxAnAaaAuthenSessionMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('local',1),(_N,2),('radius',3)))
_ZxAnAaaAuthenSessionMethod_Type.__name__=_C
_ZxAnAaaAuthenSessionMethod_Object=MibTableColumn
zxAnAaaAuthenSessionMethod=_ZxAnAaaAuthenSessionMethod_Object((1,3,6,1,4,1,3902,1015,90,2,2,2,1,2),_ZxAnAaaAuthenSessionMethod_Type())
zxAnAaaAuthenSessionMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAaaAuthenSessionMethod.setStatus(_A)
class _ZxAnAaaAuthenSessionRadiusGrpId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_ZxAnAaaAuthenSessionRadiusGrpId_Type.__name__=_C
_ZxAnAaaAuthenSessionRadiusGrpId_Object=MibTableColumn
zxAnAaaAuthenSessionRadiusGrpId=_ZxAnAaaAuthenSessionRadiusGrpId_Object((1,3,6,1,4,1,3902,1015,90,2,2,2,1,3),_ZxAnAaaAuthenSessionRadiusGrpId_Type())
zxAnAaaAuthenSessionRadiusGrpId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAaaAuthenSessionRadiusGrpId.setStatus(_A)
_ZxAnAaaAuthenSessionRowStatus_Type=RowStatus
_ZxAnAaaAuthenSessionRowStatus_Object=MibTableColumn
zxAnAaaAuthenSessionRowStatus=_ZxAnAaaAuthenSessionRowStatus_Object((1,3,6,1,4,1,3902,1015,90,2,2,2,1,50),_ZxAnAaaAuthenSessionRowStatus_Type())
zxAnAaaAuthenSessionRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAaaAuthenSessionRowStatus.setStatus(_A)
_ZxAnAaaAuthenticaitonLogin_ObjectIdentity=ObjectIdentity
zxAnAaaAuthenticaitonLogin=_ZxAnAaaAuthenticaitonLogin_ObjectIdentity((1,3,6,1,4,1,3902,1015,90,2,3))
_ZxAnAaaAuthenLoginTable_Object=MibTable
zxAnAaaAuthenLoginTable=_ZxAnAaaAuthenLoginTable_Object((1,3,6,1,4,1,3902,1015,90,2,3,2))
if mibBuilder.loadTexts:zxAnAaaAuthenLoginTable.setStatus(_A)
_ZxAnAaaAuthenLoginEntry_Object=MibTableRow
zxAnAaaAuthenLoginEntry=_ZxAnAaaAuthenLoginEntry_Object((1,3,6,1,4,1,3902,1015,90,2,3,2,1))
zxAnAaaAuthenLoginEntry.setIndexNames((0,_G,_O))
if mibBuilder.loadTexts:zxAnAaaAuthenLoginEntry.setStatus(_A)
class _ZxAnAaaAuthenLoginMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('login',1),('enable',2)))
_ZxAnAaaAuthenLoginMode_Type.__name__=_C
_ZxAnAaaAuthenLoginMode_Object=MibTableColumn
zxAnAaaAuthenLoginMode=_ZxAnAaaAuthenLoginMode_Object((1,3,6,1,4,1,3902,1015,90,2,3,2,1,1),_ZxAnAaaAuthenLoginMode_Type())
zxAnAaaAuthenLoginMode.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnAaaAuthenLoginMode.setStatus(_A)
class _ZxAnAaaAuthenLoginLocalPri_Type(ZxAnAaaAuthenMethodPriority):defaultValue=0
_ZxAnAaaAuthenLoginLocalPri_Type.__name__=_F
_ZxAnAaaAuthenLoginLocalPri_Object=MibTableColumn
zxAnAaaAuthenLoginLocalPri=_ZxAnAaaAuthenLoginLocalPri_Object((1,3,6,1,4,1,3902,1015,90,2,3,2,1,2),_ZxAnAaaAuthenLoginLocalPri_Type())
zxAnAaaAuthenLoginLocalPri.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAaaAuthenLoginLocalPri.setStatus(_A)
class _ZxAnAaaAuthenLoginTacacsplusPri_Type(ZxAnAaaAuthenMethodPriority):defaultValue=0
_ZxAnAaaAuthenLoginTacacsplusPri_Type.__name__=_F
_ZxAnAaaAuthenLoginTacacsplusPri_Object=MibTableColumn
zxAnAaaAuthenLoginTacacsplusPri=_ZxAnAaaAuthenLoginTacacsplusPri_Object((1,3,6,1,4,1,3902,1015,90,2,3,2,1,3),_ZxAnAaaAuthenLoginTacacsplusPri_Type())
zxAnAaaAuthenLoginTacacsplusPri.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAaaAuthenLoginTacacsplusPri.setStatus(_A)
class _ZxAnAaaAuthenLoginNoAuthMethodEn_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_ZxAnAaaAuthenLoginNoAuthMethodEn_Type.__name__=_C
_ZxAnAaaAuthenLoginNoAuthMethodEn_Object=MibTableColumn
zxAnAaaAuthenLoginNoAuthMethodEn=_ZxAnAaaAuthenLoginNoAuthMethodEn_Object((1,3,6,1,4,1,3902,1015,90,2,3,2,1,4),_ZxAnAaaAuthenLoginNoAuthMethodEn_Type())
zxAnAaaAuthenLoginNoAuthMethodEn.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAaaAuthenLoginNoAuthMethodEn.setStatus(_A)
class _ZxAnAaaAuthenLoginTacplusGrpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnAaaAuthenLoginTacplusGrpName_Type.__name__=_E
_ZxAnAaaAuthenLoginTacplusGrpName_Object=MibTableColumn
zxAnAaaAuthenLoginTacplusGrpName=_ZxAnAaaAuthenLoginTacplusGrpName_Object((1,3,6,1,4,1,3902,1015,90,2,3,2,1,5),_ZxAnAaaAuthenLoginTacplusGrpName_Type())
zxAnAaaAuthenLoginTacplusGrpName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAaaAuthenLoginTacplusGrpName.setStatus(_A)
_ZxAnAaaAuthenLoginRowStatus_Type=RowStatus
_ZxAnAaaAuthenLoginRowStatus_Object=MibTableColumn
zxAnAaaAuthenLoginRowStatus=_ZxAnAaaAuthenLoginRowStatus_Object((1,3,6,1,4,1,3902,1015,90,2,3,2,1,50),_ZxAnAaaAuthenLoginRowStatus_Type())
zxAnAaaAuthenLoginRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAaaAuthenLoginRowStatus.setStatus(_A)
_ZxAnAaaAuthorizationObjects_ObjectIdentity=ObjectIdentity
zxAnAaaAuthorizationObjects=_ZxAnAaaAuthorizationObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,90,3))
_ZxAnAaaAuthorGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnAaaAuthorGlobalObjects=_ZxAnAaaAuthorGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,90,3,1))
class _ZxAnAaaAuthorLocalPriority_Type(ZxAnAaaAuthorMethodPriority):defaultValue=0
_ZxAnAaaAuthorLocalPriority_Type.__name__=_K
_ZxAnAaaAuthorLocalPriority_Object=MibScalar
zxAnAaaAuthorLocalPriority=_ZxAnAaaAuthorLocalPriority_Object((1,3,6,1,4,1,3902,1015,90,3,1,1),_ZxAnAaaAuthorLocalPriority_Type())
zxAnAaaAuthorLocalPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAaaAuthorLocalPriority.setStatus(_A)
class _ZxAnAaaAuthorTacacsplusPriority_Type(ZxAnAaaAuthorMethodPriority):defaultValue=0
_ZxAnAaaAuthorTacacsplusPriority_Type.__name__=_K
_ZxAnAaaAuthorTacacsplusPriority_Object=MibScalar
zxAnAaaAuthorTacacsplusPriority=_ZxAnAaaAuthorTacacsplusPriority_Object((1,3,6,1,4,1,3902,1015,90,3,1,2),_ZxAnAaaAuthorTacacsplusPriority_Type())
zxAnAaaAuthorTacacsplusPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAaaAuthorTacacsplusPriority.setStatus(_A)
class _ZxAnAaaAuthorNoAuthorMethodEn_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_ZxAnAaaAuthorNoAuthorMethodEn_Type.__name__=_C
_ZxAnAaaAuthorNoAuthorMethodEn_Object=MibScalar
zxAnAaaAuthorNoAuthorMethodEn=_ZxAnAaaAuthorNoAuthorMethodEn_Object((1,3,6,1,4,1,3902,1015,90,3,1,3),_ZxAnAaaAuthorNoAuthorMethodEn_Type())
zxAnAaaAuthorNoAuthorMethodEn.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAaaAuthorNoAuthorMethodEn.setStatus(_A)
class _ZxAnAaaAuthorTacacsplusGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnAaaAuthorTacacsplusGroupName_Type.__name__=_E
_ZxAnAaaAuthorTacacsplusGroupName_Object=MibScalar
zxAnAaaAuthorTacacsplusGroupName=_ZxAnAaaAuthorTacacsplusGroupName_Object((1,3,6,1,4,1,3902,1015,90,3,1,4),_ZxAnAaaAuthorTacacsplusGroupName_Type())
zxAnAaaAuthorTacacsplusGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAaaAuthorTacacsplusGroupName.setStatus(_A)
_ZxAnAaaAuthorizationSession_ObjectIdentity=ObjectIdentity
zxAnAaaAuthorizationSession=_ZxAnAaaAuthorizationSession_ObjectIdentity((1,3,6,1,4,1,3902,1015,90,3,3))
_ZxAnAaaAuthorSessionTable_Object=MibTable
zxAnAaaAuthorSessionTable=_ZxAnAaaAuthorSessionTable_Object((1,3,6,1,4,1,3902,1015,90,3,3,2))
if mibBuilder.loadTexts:zxAnAaaAuthorSessionTable.setStatus(_A)
_ZxAnAaaAuthorSessionEntry_Object=MibTableRow
zxAnAaaAuthorSessionEntry=_ZxAnAaaAuthorSessionEntry_Object((1,3,6,1,4,1,3902,1015,90,3,3,2,1))
zxAnAaaAuthorSessionEntry.setIndexNames((0,_G,_P))
if mibBuilder.loadTexts:zxAnAaaAuthorSessionEntry.setStatus(_A)
class _ZxAnAaaAuthorSessionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),('ssh',2)))
_ZxAnAaaAuthorSessionType_Type.__name__=_C
_ZxAnAaaAuthorSessionType_Object=MibTableColumn
zxAnAaaAuthorSessionType=_ZxAnAaaAuthorSessionType_Object((1,3,6,1,4,1,3902,1015,90,3,3,2,1,1),_ZxAnAaaAuthorSessionType_Type())
zxAnAaaAuthorSessionType.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnAaaAuthorSessionType.setStatus(_A)
class _ZxAnAaaAuthorSessionMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),(_N,2)))
_ZxAnAaaAuthorSessionMethod_Type.__name__=_C
_ZxAnAaaAuthorSessionMethod_Object=MibTableColumn
zxAnAaaAuthorSessionMethod=_ZxAnAaaAuthorSessionMethod_Object((1,3,6,1,4,1,3902,1015,90,3,3,2,1,2),_ZxAnAaaAuthorSessionMethod_Type())
zxAnAaaAuthorSessionMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAaaAuthorSessionMethod.setStatus(_A)
class _ZxAnAaaAuthorSessionSshMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('nouse',1),('chap',2),('pap',3)))
_ZxAnAaaAuthorSessionSshMode_Type.__name__=_C
_ZxAnAaaAuthorSessionSshMode_Object=MibTableColumn
zxAnAaaAuthorSessionSshMode=_ZxAnAaaAuthorSessionSshMode_Object((1,3,6,1,4,1,3902,1015,90,3,3,2,1,3),_ZxAnAaaAuthorSessionSshMode_Type())
zxAnAaaAuthorSessionSshMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAaaAuthorSessionSshMode.setStatus(_A)
_ZxAnAaaAuthorSessionRowStatus_Type=RowStatus
_ZxAnAaaAuthorSessionRowStatus_Object=MibTableColumn
zxAnAaaAuthorSessionRowStatus=_ZxAnAaaAuthorSessionRowStatus_Object((1,3,6,1,4,1,3902,1015,90,3,3,2,1,50),_ZxAnAaaAuthorSessionRowStatus_Type())
zxAnAaaAuthorSessionRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAaaAuthorSessionRowStatus.setStatus(_A)
_ZxAnAaaAccountingObjects_ObjectIdentity=ObjectIdentity
zxAnAaaAccountingObjects=_ZxAnAaaAccountingObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,90,4))
_ZxAnAaaAccountPrivilege_ObjectIdentity=ObjectIdentity
zxAnAaaAccountPrivilege=_ZxAnAaaAccountPrivilege_ObjectIdentity((1,3,6,1,4,1,3902,1015,90,4,2))
_ZxAnAaaAccountPrivilegeTable_Object=MibTable
zxAnAaaAccountPrivilegeTable=_ZxAnAaaAccountPrivilegeTable_Object((1,3,6,1,4,1,3902,1015,90,4,2,2))
if mibBuilder.loadTexts:zxAnAaaAccountPrivilegeTable.setStatus(_A)
_ZxAnAaaAccountPrivilegeEntry_Object=MibTableRow
zxAnAaaAccountPrivilegeEntry=_ZxAnAaaAccountPrivilegeEntry_Object((1,3,6,1,4,1,3902,1015,90,4,2,2,1))
zxAnAaaAccountPrivilegeEntry.setIndexNames((0,_G,_Q))
if mibBuilder.loadTexts:zxAnAaaAccountPrivilegeEntry.setStatus(_A)
class _ZxAnAaaAccountUserPrivilege_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_ZxAnAaaAccountUserPrivilege_Type.__name__=_C
_ZxAnAaaAccountUserPrivilege_Object=MibTableColumn
zxAnAaaAccountUserPrivilege=_ZxAnAaaAccountUserPrivilege_Object((1,3,6,1,4,1,3902,1015,90,4,2,2,1,1),_ZxAnAaaAccountUserPrivilege_Type())
zxAnAaaAccountUserPrivilege.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnAaaAccountUserPrivilege.setStatus(_A)
class _ZxAnAaaAccountTacacsplusGrpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnAaaAccountTacacsplusGrpName_Type.__name__=_E
_ZxAnAaaAccountTacacsplusGrpName_Object=MibTableColumn
zxAnAaaAccountTacacsplusGrpName=_ZxAnAaaAccountTacacsplusGrpName_Object((1,3,6,1,4,1,3902,1015,90,4,2,2,1,2),_ZxAnAaaAccountTacacsplusGrpName_Type())
zxAnAaaAccountTacacsplusGrpName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAaaAccountTacacsplusGrpName.setStatus(_A)
_ZxAnAaaAccountPrivilegeRowStatus_Type=RowStatus
_ZxAnAaaAccountPrivilegeRowStatus_Object=MibTableColumn
zxAnAaaAccountPrivilegeRowStatus=_ZxAnAaaAccountPrivilegeRowStatus_Object((1,3,6,1,4,1,3902,1015,90,4,2,2,1,50),_ZxAnAaaAccountPrivilegeRowStatus_Type())
zxAnAaaAccountPrivilegeRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAaaAccountPrivilegeRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_G,**{_F:ZxAnAaaAuthenMethodPriority,_K:ZxAnAaaAuthorMethodPriority,'zxAnAccessCtrlAaaMib':zxAnAccessCtrlAaaMib,'zxAnAaaAuthenticationObjects':zxAnAaaAuthenticationObjects,'zxAnAaaAuthenGlobalObjects':zxAnAaaAuthenGlobalObjects,'zxAnAaaAuthenLocalPriority':zxAnAaaAuthenLocalPriority,'zxAnAaaAuthenTacacsplusPriority':zxAnAaaAuthenTacacsplusPriority,'zxAnAaaAuthenNoAuthenMethodEn':zxAnAaaAuthenNoAuthenMethodEn,'zxAnAaaAuthenTacacsplusGroupName':zxAnAaaAuthenTacacsplusGroupName,'zxAnAaaAuthenticationSession':zxAnAaaAuthenticationSession,'zxAnAaaAuthenSessionTable':zxAnAaaAuthenSessionTable,'zxAnAaaAuthenSessionEntry':zxAnAaaAuthenSessionEntry,_L:zxAnAaaAuthenSessionType,'zxAnAaaAuthenSessionMethod':zxAnAaaAuthenSessionMethod,'zxAnAaaAuthenSessionRadiusGrpId':zxAnAaaAuthenSessionRadiusGrpId,'zxAnAaaAuthenSessionRowStatus':zxAnAaaAuthenSessionRowStatus,'zxAnAaaAuthenticaitonLogin':zxAnAaaAuthenticaitonLogin,'zxAnAaaAuthenLoginTable':zxAnAaaAuthenLoginTable,'zxAnAaaAuthenLoginEntry':zxAnAaaAuthenLoginEntry,_O:zxAnAaaAuthenLoginMode,'zxAnAaaAuthenLoginLocalPri':zxAnAaaAuthenLoginLocalPri,'zxAnAaaAuthenLoginTacacsplusPri':zxAnAaaAuthenLoginTacacsplusPri,'zxAnAaaAuthenLoginNoAuthMethodEn':zxAnAaaAuthenLoginNoAuthMethodEn,'zxAnAaaAuthenLoginTacplusGrpName':zxAnAaaAuthenLoginTacplusGrpName,'zxAnAaaAuthenLoginRowStatus':zxAnAaaAuthenLoginRowStatus,'zxAnAaaAuthorizationObjects':zxAnAaaAuthorizationObjects,'zxAnAaaAuthorGlobalObjects':zxAnAaaAuthorGlobalObjects,'zxAnAaaAuthorLocalPriority':zxAnAaaAuthorLocalPriority,'zxAnAaaAuthorTacacsplusPriority':zxAnAaaAuthorTacacsplusPriority,'zxAnAaaAuthorNoAuthorMethodEn':zxAnAaaAuthorNoAuthorMethodEn,'zxAnAaaAuthorTacacsplusGroupName':zxAnAaaAuthorTacacsplusGroupName,'zxAnAaaAuthorizationSession':zxAnAaaAuthorizationSession,'zxAnAaaAuthorSessionTable':zxAnAaaAuthorSessionTable,'zxAnAaaAuthorSessionEntry':zxAnAaaAuthorSessionEntry,_P:zxAnAaaAuthorSessionType,'zxAnAaaAuthorSessionMethod':zxAnAaaAuthorSessionMethod,'zxAnAaaAuthorSessionSshMode':zxAnAaaAuthorSessionSshMode,'zxAnAaaAuthorSessionRowStatus':zxAnAaaAuthorSessionRowStatus,'zxAnAaaAccountingObjects':zxAnAaaAccountingObjects,'zxAnAaaAccountPrivilege':zxAnAaaAccountPrivilege,'zxAnAaaAccountPrivilegeTable':zxAnAaaAccountPrivilegeTable,'zxAnAaaAccountPrivilegeEntry':zxAnAaaAccountPrivilegeEntry,_Q:zxAnAaaAccountUserPrivilege,'zxAnAaaAccountTacacsplusGrpName':zxAnAaaAccountTacacsplusGrpName,'zxAnAaaAccountPrivilegeRowStatus':zxAnAaaAccountPrivilegeRowStatus})