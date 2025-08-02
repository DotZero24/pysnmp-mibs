_S='cacLoginConfigGroupRev1'
_R='cacLoginConfigGroup'
_Q='cacLockoutPeriodExt'
_P='cacLockoutPeriod'
_O='cacPrimaryMethod'
_N='cacPriorityNumber'
_M='cacEnable'
_L='seconds'
_K='cacAuthen'
_J='cacPriorityGroup'
_I='cacMaxLoginAttempt'
_H='deprecated'
_G='not-accessible'
_F='cacLoginMode'
_E='cacSession'
_D='read-write'
_C='Integer32'
_B='CISCO-AAA-CLIENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoAAAClientMIB=ModuleIdentity((1,3,6,1,4,1,9,9,158))
if mibBuilder.loadTexts:ciscoAAAClientMIB.setRevisions(('2001-11-19 00:00','2001-05-10 00:00'))
class SessionType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('telnet',1),('console',2),('http',3)))
class AuthenMethod(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('tacacs',1),('radius',2),('kerberos',3),('local',4)))
class LoginMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('login',1),('enable',2)))
_CacMIBObjects_ObjectIdentity=ObjectIdentity
cacMIBObjects=_CacMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,158,1))
_CacPriority_ObjectIdentity=ObjectIdentity
cacPriority=_CacPriority_ObjectIdentity((1,3,6,1,4,1,9,9,158,1,1))
_CacPriorityTable_Object=MibTable
cacPriorityTable=_CacPriorityTable_Object((1,3,6,1,4,1,9,9,158,1,1,1))
if mibBuilder.loadTexts:cacPriorityTable.setStatus(_A)
_CacPriorityEntry_Object=MibTableRow
cacPriorityEntry=_CacPriorityEntry_Object((1,3,6,1,4,1,9,9,158,1,1,1,1))
cacPriorityEntry.setIndexNames((0,_B,_E),(0,_B,_K),(0,_B,_F))
if mibBuilder.loadTexts:cacPriorityEntry.setStatus(_A)
_CacSession_Type=SessionType
_CacSession_Object=MibTableColumn
cacSession=_CacSession_Object((1,3,6,1,4,1,9,9,158,1,1,1,1,1),_CacSession_Type())
cacSession.setMaxAccess(_G)
if mibBuilder.loadTexts:cacSession.setStatus(_A)
_CacAuthen_Type=AuthenMethod
_CacAuthen_Object=MibTableColumn
cacAuthen=_CacAuthen_Object((1,3,6,1,4,1,9,9,158,1,1,1,1,2),_CacAuthen_Type())
cacAuthen.setMaxAccess(_G)
if mibBuilder.loadTexts:cacAuthen.setStatus(_A)
_CacLoginMode_Type=LoginMode
_CacLoginMode_Object=MibTableColumn
cacLoginMode=_CacLoginMode_Object((1,3,6,1,4,1,9,9,158,1,1,1,1,3),_CacLoginMode_Type())
cacLoginMode.setMaxAccess(_G)
if mibBuilder.loadTexts:cacLoginMode.setStatus(_A)
_CacEnable_Type=TruthValue
_CacEnable_Object=MibTableColumn
cacEnable=_CacEnable_Object((1,3,6,1,4,1,9,9,158,1,1,1,1,4),_CacEnable_Type())
cacEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cacEnable.setStatus(_A)
class _CacPriorityNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_CacPriorityNumber_Type.__name__=_C
_CacPriorityNumber_Object=MibTableColumn
cacPriorityNumber=_CacPriorityNumber_Object((1,3,6,1,4,1,9,9,158,1,1,1,1,5),_CacPriorityNumber_Type())
cacPriorityNumber.setMaxAccess('read-only')
if mibBuilder.loadTexts:cacPriorityNumber.setStatus(_A)
_CacPrimaryMethod_Type=TruthValue
_CacPrimaryMethod_Object=MibTableColumn
cacPrimaryMethod=_CacPrimaryMethod_Object((1,3,6,1,4,1,9,9,158,1,1,1,1,6),_CacPrimaryMethod_Type())
cacPrimaryMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:cacPrimaryMethod.setStatus(_A)
_CacLoginConfig_ObjectIdentity=ObjectIdentity
cacLoginConfig=_CacLoginConfig_ObjectIdentity((1,3,6,1,4,1,9,9,158,1,2))
_CacLoginConfigTable_Object=MibTable
cacLoginConfigTable=_CacLoginConfigTable_Object((1,3,6,1,4,1,9,9,158,1,2,1))
if mibBuilder.loadTexts:cacLoginConfigTable.setStatus(_A)
_CacLoginConfigEntry_Object=MibTableRow
cacLoginConfigEntry=_CacLoginConfigEntry_Object((1,3,6,1,4,1,9,9,158,1,2,1,1))
cacLoginConfigEntry.setIndexNames((0,_B,_F),(0,_B,_E))
if mibBuilder.loadTexts:cacLoginConfigEntry.setStatus(_A)
class _CacMaxLoginAttempt_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,10))
_CacMaxLoginAttempt_Type.__name__=_C
_CacMaxLoginAttempt_Object=MibTableColumn
cacMaxLoginAttempt=_CacMaxLoginAttempt_Object((1,3,6,1,4,1,9,9,158,1,2,1,1,1),_CacMaxLoginAttempt_Type())
cacMaxLoginAttempt.setMaxAccess(_D)
if mibBuilder.loadTexts:cacMaxLoginAttempt.setStatus(_A)
class _CacLockoutPeriod_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(30,600))
_CacLockoutPeriod_Type.__name__=_C
_CacLockoutPeriod_Object=MibTableColumn
cacLockoutPeriod=_CacLockoutPeriod_Object((1,3,6,1,4,1,9,9,158,1,2,1,1,2),_CacLockoutPeriod_Type())
cacLockoutPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:cacLockoutPeriod.setStatus(_H)
if mibBuilder.loadTexts:cacLockoutPeriod.setUnits(_L)
class _CacLockoutPeriodExt_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(30,43200))
_CacLockoutPeriodExt_Type.__name__=_C
_CacLockoutPeriodExt_Object=MibTableColumn
cacLockoutPeriodExt=_CacLockoutPeriodExt_Object((1,3,6,1,4,1,9,9,158,1,2,1,1,3),_CacLockoutPeriodExt_Type())
cacLockoutPeriodExt.setMaxAccess(_D)
if mibBuilder.loadTexts:cacLockoutPeriodExt.setStatus(_A)
if mibBuilder.loadTexts:cacLockoutPeriodExt.setUnits(_L)
_CacMIBNotifications_ObjectIdentity=ObjectIdentity
cacMIBNotifications=_CacMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,158,2))
_CacMIBConformance_ObjectIdentity=ObjectIdentity
cacMIBConformance=_CacMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,158,3))
_CacMIBCompliances_ObjectIdentity=ObjectIdentity
cacMIBCompliances=_CacMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,158,3,1))
_CacMIBGroups_ObjectIdentity=ObjectIdentity
cacMIBGroups=_CacMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,158,3,2))
cacPriorityGroup=ObjectGroup((1,3,6,1,4,1,9,9,158,3,2,1))
cacPriorityGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:cacPriorityGroup.setStatus(_A)
cacLoginConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,158,3,2,2))
cacLoginConfigGroup.setObjects(*((_B,_I),(_B,_P)))
if mibBuilder.loadTexts:cacLoginConfigGroup.setStatus(_H)
cacLoginConfigGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,158,3,2,3))
cacLoginConfigGroupRev1.setObjects(*((_B,_I),(_B,_Q)))
if mibBuilder.loadTexts:cacLoginConfigGroupRev1.setStatus(_A)
cacMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,158,3,1,1))
cacMIBCompliance.setObjects(*((_B,_J),(_B,_R)))
if mibBuilder.loadTexts:cacMIBCompliance.setStatus(_H)
cacMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,158,3,1,2))
cacMIBCompliance2.setObjects(*((_B,_J),(_B,_S)))
if mibBuilder.loadTexts:cacMIBCompliance2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SessionType':SessionType,'AuthenMethod':AuthenMethod,'LoginMode':LoginMode,'ciscoAAAClientMIB':ciscoAAAClientMIB,'cacMIBObjects':cacMIBObjects,'cacPriority':cacPriority,'cacPriorityTable':cacPriorityTable,'cacPriorityEntry':cacPriorityEntry,_E:cacSession,_K:cacAuthen,_F:cacLoginMode,_M:cacEnable,_N:cacPriorityNumber,_O:cacPrimaryMethod,'cacLoginConfig':cacLoginConfig,'cacLoginConfigTable':cacLoginConfigTable,'cacLoginConfigEntry':cacLoginConfigEntry,_I:cacMaxLoginAttempt,_P:cacLockoutPeriod,_Q:cacLockoutPeriodExt,'cacMIBNotifications':cacMIBNotifications,'cacMIBConformance':cacMIBConformance,'cacMIBCompliances':cacMIBCompliances,'cacMIBCompliance':cacMIBCompliance,'cacMIBCompliance2':cacMIBCompliance2,'cacMIBGroups':cacMIBGroups,_J:cacPriorityGroup,_R:cacLoginConfigGroup,_S:cacLoginConfigGroupRev1})