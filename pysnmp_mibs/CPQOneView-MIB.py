_U='NotificationType'
_T='mandatory'
_S='Integer32'
_R='cpqOneViewAlertInfo'
_Q='cpqOneViewAlertTypeId'
_P='cpqOneViewAlertEnterpriseId'
_O='cpqOneViewAlertSourceIPv6Address'
_N='cpqOneViewAlertSourceIPv4Address'
_M='cpqOneViewAlertResourceUri'
_L='cpqOneViewAlertResourceType'
_K='cpqOneViewAlertCreatedTime'
_J='cpqOneViewAlertIsLifecycle'
_I='cpqOneViewAlertResolution'
_H='cpqOneViewAlertSummary'
_G='cpqOneViewAlertState'
_F='cpqOneViewAlertCategory'
_E='sysName'
_D='SNMPv2-MIB'
_C='optional'
_B='read-only'
_A='CPQOneView-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,cpqHoTrapFlags=mibBuilder.importSymbols('CPQHOST-MIB','compaq','cpqHoTrapFlags')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_D,_E)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_S,'IpAddress','ModuleIdentity','MibIdentifier',_U,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_U,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CpqOneView_ObjectIdentity=ObjectIdentity
cpqOneView=_CpqOneView_ObjectIdentity((1,3,6,1,4,1,232,179))
_CpqOneViewMibRev_ObjectIdentity=ObjectIdentity
cpqOneViewMibRev=_CpqOneViewMibRev_ObjectIdentity((1,3,6,1,4,1,232,179,1))
class _CpqOneViewMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqOneViewMibRevMajor_Type.__name__=_S
_CpqOneViewMibRevMajor_Object=MibScalar
cpqOneViewMibRevMajor=_CpqOneViewMibRevMajor_Object((1,3,6,1,4,1,232,179,1,1),_CpqOneViewMibRevMajor_Type())
cpqOneViewMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOneViewMibRevMajor.setStatus(_T)
class _CpqOneViewMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqOneViewMibRevMinor_Type.__name__=_S
_CpqOneViewMibRevMinor_Object=MibScalar
cpqOneViewMibRevMinor=_CpqOneViewMibRevMinor_Object((1,3,6,1,4,1,232,179,1,2),_CpqOneViewMibRevMinor_Type())
cpqOneViewMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOneViewMibRevMinor.setStatus(_T)
class _CpqOneViewMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('ok',2),('degraded',3),('failed',4)))
_CpqOneViewMibCondition_Type.__name__=_S
_CpqOneViewMibCondition_Object=MibScalar
cpqOneViewMibCondition=_CpqOneViewMibCondition_Object((1,3,6,1,4,1,232,179,1,3),_CpqOneViewMibCondition_Type())
cpqOneViewMibCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOneViewMibCondition.setStatus(_T)
_CpqOneViewComponent_ObjectIdentity=ObjectIdentity
cpqOneViewComponent=_CpqOneViewComponent_ObjectIdentity((1,3,6,1,4,1,232,179,2))
_CpqOneViewAlert_ObjectIdentity=ObjectIdentity
cpqOneViewAlert=_CpqOneViewAlert_ObjectIdentity((1,3,6,1,4,1,232,179,2,1))
_CpqOneViewAlertSummary_Type=DisplayString
_CpqOneViewAlertSummary_Object=MibScalar
cpqOneViewAlertSummary=_CpqOneViewAlertSummary_Object((1,3,6,1,4,1,232,179,2,1,1),_CpqOneViewAlertSummary_Type())
cpqOneViewAlertSummary.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOneViewAlertSummary.setStatus(_C)
_CpqOneViewAlertResolution_Type=DisplayString
_CpqOneViewAlertResolution_Object=MibScalar
cpqOneViewAlertResolution=_CpqOneViewAlertResolution_Object((1,3,6,1,4,1,232,179,2,1,2),_CpqOneViewAlertResolution_Type())
cpqOneViewAlertResolution.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOneViewAlertResolution.setStatus(_C)
_CpqOneViewAlertCategory_Type=DisplayString
_CpqOneViewAlertCategory_Object=MibScalar
cpqOneViewAlertCategory=_CpqOneViewAlertCategory_Object((1,3,6,1,4,1,232,179,2,1,3),_CpqOneViewAlertCategory_Type())
cpqOneViewAlertCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOneViewAlertCategory.setStatus(_C)
_CpqOneViewAlertState_Type=DisplayString
_CpqOneViewAlertState_Object=MibScalar
cpqOneViewAlertState=_CpqOneViewAlertState_Object((1,3,6,1,4,1,232,179,2,1,4),_CpqOneViewAlertState_Type())
cpqOneViewAlertState.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOneViewAlertState.setStatus(_C)
_CpqOneViewAlertIsLifecycle_Type=DisplayString
_CpqOneViewAlertIsLifecycle_Object=MibScalar
cpqOneViewAlertIsLifecycle=_CpqOneViewAlertIsLifecycle_Object((1,3,6,1,4,1,232,179,2,1,5),_CpqOneViewAlertIsLifecycle_Type())
cpqOneViewAlertIsLifecycle.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOneViewAlertIsLifecycle.setStatus(_C)
_CpqOneViewAlertResourceType_Type=DisplayString
_CpqOneViewAlertResourceType_Object=MibScalar
cpqOneViewAlertResourceType=_CpqOneViewAlertResourceType_Object((1,3,6,1,4,1,232,179,2,1,6),_CpqOneViewAlertResourceType_Type())
cpqOneViewAlertResourceType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOneViewAlertResourceType.setStatus(_C)
_CpqOneViewAlertResourceUri_Type=DisplayString
_CpqOneViewAlertResourceUri_Object=MibScalar
cpqOneViewAlertResourceUri=_CpqOneViewAlertResourceUri_Object((1,3,6,1,4,1,232,179,2,1,7),_CpqOneViewAlertResourceUri_Type())
cpqOneViewAlertResourceUri.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOneViewAlertResourceUri.setStatus(_C)
_CpqOneViewAlertCreatedTime_Type=DisplayString
_CpqOneViewAlertCreatedTime_Object=MibScalar
cpqOneViewAlertCreatedTime=_CpqOneViewAlertCreatedTime_Object((1,3,6,1,4,1,232,179,2,1,8),_CpqOneViewAlertCreatedTime_Type())
cpqOneViewAlertCreatedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOneViewAlertCreatedTime.setStatus(_C)
_CpqOneViewAlertDeviceHealth_ObjectIdentity=ObjectIdentity
cpqOneViewAlertDeviceHealth=_CpqOneViewAlertDeviceHealth_ObjectIdentity((1,3,6,1,4,1,232,179,2,1,100))
_CpqOneViewAlertSourceIPv4Address_Type=IpAddress
_CpqOneViewAlertSourceIPv4Address_Object=MibScalar
cpqOneViewAlertSourceIPv4Address=_CpqOneViewAlertSourceIPv4Address_Object((1,3,6,1,4,1,232,179,2,1,100,1),_CpqOneViewAlertSourceIPv4Address_Type())
cpqOneViewAlertSourceIPv4Address.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOneViewAlertSourceIPv4Address.setStatus(_C)
_CpqOneViewAlertSourceIPv6Address_Type=IpAddress
_CpqOneViewAlertSourceIPv6Address_Object=MibScalar
cpqOneViewAlertSourceIPv6Address=_CpqOneViewAlertSourceIPv6Address_Object((1,3,6,1,4,1,232,179,2,1,100,2),_CpqOneViewAlertSourceIPv6Address_Type())
cpqOneViewAlertSourceIPv6Address.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOneViewAlertSourceIPv6Address.setStatus(_C)
_CpqOneViewAlertEnterpriseId_Type=DisplayString
_CpqOneViewAlertEnterpriseId_Object=MibScalar
cpqOneViewAlertEnterpriseId=_CpqOneViewAlertEnterpriseId_Object((1,3,6,1,4,1,232,179,2,1,100,3),_CpqOneViewAlertEnterpriseId_Type())
cpqOneViewAlertEnterpriseId.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOneViewAlertEnterpriseId.setStatus(_C)
_CpqOneViewAlertTypeId_Type=Integer32
_CpqOneViewAlertTypeId_Object=MibScalar
cpqOneViewAlertTypeId=_CpqOneViewAlertTypeId_Object((1,3,6,1,4,1,232,179,2,1,100,4),_CpqOneViewAlertTypeId_Type())
cpqOneViewAlertTypeId.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOneViewAlertTypeId.setStatus(_C)
_CpqOneViewAlertInfo_Type=Integer32
_CpqOneViewAlertInfo_Object=MibScalar
cpqOneViewAlertInfo=_CpqOneViewAlertInfo_Object((1,3,6,1,4,1,232,179,2,1,100,5),_CpqOneViewAlertInfo_Type())
cpqOneViewAlertInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOneViewAlertInfo.setStatus(_C)
cpqOneViewCriticalAlert=NotificationType((1,3,6,1,4,1,232,0,179001))
cpqOneViewCriticalAlert.setObjects(*((_D,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:cpqOneViewCriticalAlert.setStatus('')
cpqOneViewWarningAlert=NotificationType((1,3,6,1,4,1,232,0,179002))
cpqOneViewWarningAlert.setObjects(*((_D,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:cpqOneViewWarningAlert.setStatus('')
cpqOneViewOkAlert=NotificationType((1,3,6,1,4,1,232,0,179003))
cpqOneViewOkAlert.setObjects(*((_D,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:cpqOneViewOkAlert.setStatus('')
cpqOneViewUnknownAlert=NotificationType((1,3,6,1,4,1,232,0,179004))
cpqOneViewUnknownAlert.setObjects(*((_D,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:cpqOneViewUnknownAlert.setStatus('')
mibBuilder.exportSymbols(_A,**{'cpqOneViewCriticalAlert':cpqOneViewCriticalAlert,'cpqOneViewWarningAlert':cpqOneViewWarningAlert,'cpqOneViewOkAlert':cpqOneViewOkAlert,'cpqOneViewUnknownAlert':cpqOneViewUnknownAlert,'cpqOneView':cpqOneView,'cpqOneViewMibRev':cpqOneViewMibRev,'cpqOneViewMibRevMajor':cpqOneViewMibRevMajor,'cpqOneViewMibRevMinor':cpqOneViewMibRevMinor,'cpqOneViewMibCondition':cpqOneViewMibCondition,'cpqOneViewComponent':cpqOneViewComponent,'cpqOneViewAlert':cpqOneViewAlert,_H:cpqOneViewAlertSummary,_I:cpqOneViewAlertResolution,_F:cpqOneViewAlertCategory,_G:cpqOneViewAlertState,_J:cpqOneViewAlertIsLifecycle,_L:cpqOneViewAlertResourceType,_M:cpqOneViewAlertResourceUri,_K:cpqOneViewAlertCreatedTime,'cpqOneViewAlertDeviceHealth':cpqOneViewAlertDeviceHealth,_N:cpqOneViewAlertSourceIPv4Address,_O:cpqOneViewAlertSourceIPv6Address,_P:cpqOneViewAlertEnterpriseId,_Q:cpqOneViewAlertTypeId,_R:cpqOneViewAlertInfo})