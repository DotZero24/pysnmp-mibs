_P='hm2TsnTemplateBasedParametersEntry'
_O='hm2STParametersEntry'
_N='tc7GbTc6Tc5to0Gb'
_M='gbTc7Tc5to0GbTc6'
_L='gbTc6GbTc7Tc5to0'
_K='tc5to0GbTc7GbTc6'
_J='gbTc7GbTc6Tc5to0'
_I='tc6to0GbTc7'
_H='gbTc7Tc6to0'
_G='tc7Tc6to0Gb'
_F='HmEnabledStatus'
_E='HM2-TSN-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HmEnabledStatus,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_F,'hm2ConfigurationMibs')
ieee8021STParametersEntry,=mibBuilder.importSymbols('IEEE8021-ST-MIB','ieee8021STParametersEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hm2TsnMib=ModuleIdentity((1,3,6,1,4,1,248,11,51))
if mibBuilder.loadTexts:hm2TsnMib.setRevisions(('2018-02-06 00:00','2021-02-19 00:00','2021-03-15 00:00'))
class Hm2TsnBaseTime(TextualConvention,OctetString):status=_A;displayHint='2d-1d-1d,1d:1d:1d.4d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(11,11));fixedLength=11
_Hm2TsnNotifications_ObjectIdentity=ObjectIdentity
hm2TsnNotifications=_Hm2TsnNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,51,0))
_Hm2TsnMibObjects_ObjectIdentity=ObjectIdentity
hm2TsnMibObjects=_Hm2TsnMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,51,1))
_Hm2TsnGroup_ObjectIdentity=ObjectIdentity
hm2TsnGroup=_Hm2TsnGroup_ObjectIdentity((1,3,6,1,4,1,248,11,51,1,1))
class _Hm2TsnAdminState_Type(HmEnabledStatus):defaultValue=2
_Hm2TsnAdminState_Type.__name__=_F
_Hm2TsnAdminState_Object=MibScalar
hm2TsnAdminState=_Hm2TsnAdminState_Object((1,3,6,1,4,1,248,11,51,1,1,1),_Hm2TsnAdminState_Type())
hm2TsnAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2TsnAdminState.setStatus(_A)
_Hm2STParametersTable_Object=MibTable
hm2STParametersTable=_Hm2STParametersTable_Object((1,3,6,1,4,1,248,11,51,1,2))
if mibBuilder.loadTexts:hm2STParametersTable.setStatus(_A)
_Hm2STParametersEntry_Object=MibTableRow
hm2STParametersEntry=_Hm2STParametersEntry_Object((1,3,6,1,4,1,248,11,51,1,2,1))
if mibBuilder.loadTexts:hm2STParametersEntry.setStatus(_A)
_Hm2STAdminBaseTime_Type=Hm2TsnBaseTime
_Hm2STAdminBaseTime_Object=MibTableColumn
hm2STAdminBaseTime=_Hm2STAdminBaseTime_Object((1,3,6,1,4,1,248,11,51,1,2,1,1),_Hm2STAdminBaseTime_Type())
hm2STAdminBaseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2STAdminBaseTime.setStatus(_A)
_Hm2STOperBaseTime_Type=Hm2TsnBaseTime
_Hm2STOperBaseTime_Object=MibTableColumn
hm2STOperBaseTime=_Hm2STOperBaseTime_Object((1,3,6,1,4,1,248,11,51,1,2,1,2),_Hm2STOperBaseTime_Type())
hm2STOperBaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2STOperBaseTime.setStatus(_A)
_Hm2STConfigChangeTime_Type=Hm2TsnBaseTime
_Hm2STConfigChangeTime_Object=MibTableColumn
hm2STConfigChangeTime=_Hm2STConfigChangeTime_Object((1,3,6,1,4,1,248,11,51,1,2,1,3),_Hm2STConfigChangeTime_Type())
hm2STConfigChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2STConfigChangeTime.setStatus(_A)
class _Hm2STPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('running',1),('waitForTimeSync',2),('pending',3),('disabled',4),('error',5)))
_Hm2STPortStatus_Type.__name__=_B
_Hm2STPortStatus_Object=MibTableColumn
hm2STPortStatus=_Hm2STPortStatus_Object((1,3,6,1,4,1,248,11,51,1,2,1,4),_Hm2STPortStatus_Type())
hm2STPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2STPortStatus.setStatus(_A)
_Hm2TsnTemplateBasedGroup_ObjectIdentity=ObjectIdentity
hm2TsnTemplateBasedGroup=_Hm2TsnTemplateBasedGroup_ObjectIdentity((1,3,6,1,4,1,248,11,51,1,3))
_Hm2TsnTemplateBasedParametersTable_Object=MibTable
hm2TsnTemplateBasedParametersTable=_Hm2TsnTemplateBasedParametersTable_Object((1,3,6,1,4,1,248,11,51,1,3,1))
if mibBuilder.loadTexts:hm2TsnTemplateBasedParametersTable.setStatus(_A)
_Hm2TsnTemplateBasedParametersEntry_Object=MibTableRow
hm2TsnTemplateBasedParametersEntry=_Hm2TsnTemplateBasedParametersEntry_Object((1,3,6,1,4,1,248,11,51,1,3,1,1))
if mibBuilder.loadTexts:hm2TsnTemplateBasedParametersEntry.setStatus(_A)
class _Hm2TsnAdminTemplateGcl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('noop',1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7),(_M,8),(_N,9)))
_Hm2TsnAdminTemplateGcl_Type.__name__=_B
_Hm2TsnAdminTemplateGcl_Object=MibTableColumn
hm2TsnAdminTemplateGcl=_Hm2TsnAdminTemplateGcl_Object((1,3,6,1,4,1,248,11,51,1,3,1,1,1),_Hm2TsnAdminTemplateGcl_Type())
hm2TsnAdminTemplateGcl.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2TsnAdminTemplateGcl.setStatus(_A)
class _Hm2TsnOperTemplateGcl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('noTemplate',1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7),(_M,8),(_N,9)))
_Hm2TsnOperTemplateGcl_Type.__name__=_B
_Hm2TsnOperTemplateGcl_Object=MibTableColumn
hm2TsnOperTemplateGcl=_Hm2TsnOperTemplateGcl_Object((1,3,6,1,4,1,248,11,51,1,3,1,1,2),_Hm2TsnOperTemplateGcl_Type())
hm2TsnOperTemplateGcl.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2TsnOperTemplateGcl.setStatus(_A)
_Hm2TsnMibSNMPExtensionGroup_ObjectIdentity=ObjectIdentity
hm2TsnMibSNMPExtensionGroup=_Hm2TsnMibSNMPExtensionGroup_ObjectIdentity((1,3,6,1,4,1,248,11,51,3))
_Hm2TsnConflictMibSESGroup_ObjectIdentity=ObjectIdentity
hm2TsnConflictMibSESGroup=_Hm2TsnConflictMibSESGroup_ObjectIdentity((1,3,6,1,4,1,248,11,51,3,1))
_Hm2TsnGranulaityConflict_ObjectIdentity=ObjectIdentity
hm2TsnGranulaityConflict=_Hm2TsnGranulaityConflict_ObjectIdentity((1,3,6,1,4,1,248,11,51,3,1,1))
if mibBuilder.loadTexts:hm2TsnGranulaityConflict.setStatus(_A)
_Hm2TsnGCLTimeIntervalConflit_ObjectIdentity=ObjectIdentity
hm2TsnGCLTimeIntervalConflit=_Hm2TsnGCLTimeIntervalConflit_ObjectIdentity((1,3,6,1,4,1,248,11,51,3,1,2))
if mibBuilder.loadTexts:hm2TsnGCLTimeIntervalConflit.setStatus(_A)
_Hm2TsnGCLTemplateConflict_ObjectIdentity=ObjectIdentity
hm2TsnGCLTemplateConflict=_Hm2TsnGCLTemplateConflict_ObjectIdentity((1,3,6,1,4,1,248,11,51,3,1,3))
if mibBuilder.loadTexts:hm2TsnGCLTemplateConflict.setStatus(_A)
ieee8021STParametersEntry.registerAugmentions((_E,_O))
hm2STParametersEntry.setIndexNames(*ieee8021STParametersEntry.getIndexNames())
ieee8021STParametersEntry.registerAugmentions((_E,_P))
hm2TsnTemplateBasedParametersEntry.setIndexNames(*ieee8021STParametersEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{'Hm2TsnBaseTime':Hm2TsnBaseTime,'hm2TsnMib':hm2TsnMib,'hm2TsnNotifications':hm2TsnNotifications,'hm2TsnMibObjects':hm2TsnMibObjects,'hm2TsnGroup':hm2TsnGroup,'hm2TsnAdminState':hm2TsnAdminState,'hm2STParametersTable':hm2STParametersTable,_O:hm2STParametersEntry,'hm2STAdminBaseTime':hm2STAdminBaseTime,'hm2STOperBaseTime':hm2STOperBaseTime,'hm2STConfigChangeTime':hm2STConfigChangeTime,'hm2STPortStatus':hm2STPortStatus,'hm2TsnTemplateBasedGroup':hm2TsnTemplateBasedGroup,'hm2TsnTemplateBasedParametersTable':hm2TsnTemplateBasedParametersTable,_P:hm2TsnTemplateBasedParametersEntry,'hm2TsnAdminTemplateGcl':hm2TsnAdminTemplateGcl,'hm2TsnOperTemplateGcl':hm2TsnOperTemplateGcl,'hm2TsnMibSNMPExtensionGroup':hm2TsnMibSNMPExtensionGroup,'hm2TsnConflictMibSESGroup':hm2TsnConflictMibSESGroup,'hm2TsnGranulaityConflict':hm2TsnGranulaityConflict,'hm2TsnGCLTimeIntervalConflit':hm2TsnGCLTimeIntervalConflit,'hm2TsnGCLTemplateConflict':hm2TsnGCLTemplateConflict})