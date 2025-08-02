_L='hpnicfRCPSessionId'
_K='hpnicfRCPClientIP'
_J='hpnicfRCPClientIPType'
_I='hpnicfRCPUserName'
_H='Integer32'
_G='DisplayString'
_F='not-accessible'
_E='read-write'
_D='read-create'
_C='HPN-ICF-RCP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfRCP,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfRCP')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention','TruthValue')
hpnicfRCPMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,73,1))
if mibBuilder.loadTexts:hpnicfRCPMIB.setRevisions(('2006-09-20 00:00',))
_HpnicfRCPLeaf_ObjectIdentity=ObjectIdentity
hpnicfRCPLeaf=_HpnicfRCPLeaf_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,73,1,1))
_HpnicfRCPServerEnableStatus_Type=TruthValue
_HpnicfRCPServerEnableStatus_Object=MibScalar
hpnicfRCPServerEnableStatus=_HpnicfRCPServerEnableStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,1,1),_HpnicfRCPServerEnableStatus_Type())
hpnicfRCPServerEnableStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRCPServerEnableStatus.setStatus(_A)
_HpnicfRCPConnTimeout_Type=Integer32
_HpnicfRCPConnTimeout_Object=MibScalar
hpnicfRCPConnTimeout=_HpnicfRCPConnTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,1,2),_HpnicfRCPConnTimeout_Type())
hpnicfRCPConnTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRCPConnTimeout.setStatus(_A)
_HpnicfRCPRuleTimeout_Type=Integer32
_HpnicfRCPRuleTimeout_Object=MibScalar
hpnicfRCPRuleTimeout=_HpnicfRCPRuleTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,1,3),_HpnicfRCPRuleTimeout_Type())
hpnicfRCPRuleTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRCPRuleTimeout.setStatus(_A)
_HpnicfRCPServerMaxConn_Type=Integer32
_HpnicfRCPServerMaxConn_Object=MibScalar
hpnicfRCPServerMaxConn=_HpnicfRCPServerMaxConn_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,1,4),_HpnicfRCPServerMaxConn_Type())
hpnicfRCPServerMaxConn.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRCPServerMaxConn.setStatus(_A)
_HpnicfRCPServerCurConn_Type=Integer32
_HpnicfRCPServerCurConn_Object=MibScalar
hpnicfRCPServerCurConn=_HpnicfRCPServerCurConn_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,1,5),_HpnicfRCPServerCurConn_Type())
hpnicfRCPServerCurConn.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRCPServerCurConn.setStatus(_A)
_HpnicfRCPConnTimeoutMaxValue_Type=Integer32
_HpnicfRCPConnTimeoutMaxValue_Object=MibScalar
hpnicfRCPConnTimeoutMaxValue=_HpnicfRCPConnTimeoutMaxValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,1,6),_HpnicfRCPConnTimeoutMaxValue_Type())
hpnicfRCPConnTimeoutMaxValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRCPConnTimeoutMaxValue.setStatus(_A)
_HpnicfRCPRuleTimeoutMaxValue_Type=Integer32
_HpnicfRCPRuleTimeoutMaxValue_Object=MibScalar
hpnicfRCPRuleTimeoutMaxValue=_HpnicfRCPRuleTimeoutMaxValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,1,7),_HpnicfRCPRuleTimeoutMaxValue_Type())
hpnicfRCPRuleTimeoutMaxValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRCPRuleTimeoutMaxValue.setStatus(_A)
_HpnicfRCPServerMaxConnMaxValue_Type=Integer32
_HpnicfRCPServerMaxConnMaxValue_Object=MibScalar
hpnicfRCPServerMaxConnMaxValue=_HpnicfRCPServerMaxConnMaxValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,1,8),_HpnicfRCPServerMaxConnMaxValue_Type())
hpnicfRCPServerMaxConnMaxValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRCPServerMaxConnMaxValue.setStatus(_A)
_HpnicfRCPBalanceGroupIdMinValue_Type=Integer32
_HpnicfRCPBalanceGroupIdMinValue_Object=MibScalar
hpnicfRCPBalanceGroupIdMinValue=_HpnicfRCPBalanceGroupIdMinValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,1,9),_HpnicfRCPBalanceGroupIdMinValue_Type())
hpnicfRCPBalanceGroupIdMinValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRCPBalanceGroupIdMinValue.setStatus(_A)
_HpnicfRCPBalanceGroupIdMaxValue_Type=Integer32
_HpnicfRCPBalanceGroupIdMaxValue_Object=MibScalar
hpnicfRCPBalanceGroupIdMaxValue=_HpnicfRCPBalanceGroupIdMaxValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,1,10),_HpnicfRCPBalanceGroupIdMaxValue_Type())
hpnicfRCPBalanceGroupIdMaxValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRCPBalanceGroupIdMaxValue.setStatus(_A)
_HpnicfRCPTotalUsers_Type=Integer32
_HpnicfRCPTotalUsers_Object=MibScalar
hpnicfRCPTotalUsers=_HpnicfRCPTotalUsers_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,1,11),_HpnicfRCPTotalUsers_Type())
hpnicfRCPTotalUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRCPTotalUsers.setStatus(_A)
_HpnicfRCPTotalClientIPs_Type=Integer32
_HpnicfRCPTotalClientIPs_Object=MibScalar
hpnicfRCPTotalClientIPs=_HpnicfRCPTotalClientIPs_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,1,12),_HpnicfRCPTotalClientIPs_Type())
hpnicfRCPTotalClientIPs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRCPTotalClientIPs.setStatus(_A)
_HpnicfRCPTable_ObjectIdentity=ObjectIdentity
hpnicfRCPTable=_HpnicfRCPTable_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,73,1,2))
_HpnicfRCPUserTable_Object=MibTable
hpnicfRCPUserTable=_HpnicfRCPUserTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,2,1))
if mibBuilder.loadTexts:hpnicfRCPUserTable.setStatus(_A)
_HpnicfRCPUserEntry_Object=MibTableRow
hpnicfRCPUserEntry=_HpnicfRCPUserEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,2,1,1))
hpnicfRCPUserEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:hpnicfRCPUserEntry.setStatus(_A)
class _HpnicfRCPUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_HpnicfRCPUserName_Type.__name__=_G
_HpnicfRCPUserName_Object=MibTableColumn
hpnicfRCPUserName=_HpnicfRCPUserName_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,2,1,1,1),_HpnicfRCPUserName_Type())
hpnicfRCPUserName.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRCPUserName.setStatus(_A)
class _HpnicfRCPUserPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_HpnicfRCPUserPassword_Type.__name__=_G
_HpnicfRCPUserPassword_Object=MibTableColumn
hpnicfRCPUserPassword=_HpnicfRCPUserPassword_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,2,1,1,2),_HpnicfRCPUserPassword_Type())
hpnicfRCPUserPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfRCPUserPassword.setStatus(_A)
_HpnicfRCPUserRedirectInterface_Type=InterfaceIndexOrZero
_HpnicfRCPUserRedirectInterface_Object=MibTableColumn
hpnicfRCPUserRedirectInterface=_HpnicfRCPUserRedirectInterface_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,2,1,1,3),_HpnicfRCPUserRedirectInterface_Type())
hpnicfRCPUserRedirectInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfRCPUserRedirectInterface.setStatus(_A)
_HpnicfRCPUserRedirectBalanceGroup_Type=Integer32
_HpnicfRCPUserRedirectBalanceGroup_Object=MibTableColumn
hpnicfRCPUserRedirectBalanceGroup=_HpnicfRCPUserRedirectBalanceGroup_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,2,1,1,4),_HpnicfRCPUserRedirectBalanceGroup_Type())
hpnicfRCPUserRedirectBalanceGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfRCPUserRedirectBalanceGroup.setStatus(_A)
_HpnicfRCPUserRowStatus_Type=RowStatus
_HpnicfRCPUserRowStatus_Object=MibTableColumn
hpnicfRCPUserRowStatus=_HpnicfRCPUserRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,2,1,1,5),_HpnicfRCPUserRowStatus_Type())
hpnicfRCPUserRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfRCPUserRowStatus.setStatus(_A)
_HpnicfRCPClientIPTable_Object=MibTable
hpnicfRCPClientIPTable=_HpnicfRCPClientIPTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,2,2))
if mibBuilder.loadTexts:hpnicfRCPClientIPTable.setStatus(_A)
_HpnicfRCPClientIPEntry_Object=MibTableRow
hpnicfRCPClientIPEntry=_HpnicfRCPClientIPEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,2,2,1))
hpnicfRCPClientIPEntry.setIndexNames((0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:hpnicfRCPClientIPEntry.setStatus(_A)
_HpnicfRCPClientIPType_Type=InetAddressType
_HpnicfRCPClientIPType_Object=MibTableColumn
hpnicfRCPClientIPType=_HpnicfRCPClientIPType_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,2,2,1,1),_HpnicfRCPClientIPType_Type())
hpnicfRCPClientIPType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRCPClientIPType.setStatus(_A)
_HpnicfRCPClientIP_Type=InetAddress
_HpnicfRCPClientIP_Object=MibTableColumn
hpnicfRCPClientIP=_HpnicfRCPClientIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,2,2,1,2),_HpnicfRCPClientIP_Type())
hpnicfRCPClientIP.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRCPClientIP.setStatus(_A)
_HpnicfRCPClientIPRowStatus_Type=RowStatus
_HpnicfRCPClientIPRowStatus_Object=MibTableColumn
hpnicfRCPClientIPRowStatus=_HpnicfRCPClientIPRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,2,2,1,3),_HpnicfRCPClientIPRowStatus_Type())
hpnicfRCPClientIPRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfRCPClientIPRowStatus.setStatus(_A)
_HpnicfRCPSessionTable_Object=MibTable
hpnicfRCPSessionTable=_HpnicfRCPSessionTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,2,3))
if mibBuilder.loadTexts:hpnicfRCPSessionTable.setStatus(_A)
_HpnicfRCPSessionEntry_Object=MibTableRow
hpnicfRCPSessionEntry=_HpnicfRCPSessionEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,2,3,1))
hpnicfRCPSessionEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:hpnicfRCPSessionEntry.setStatus(_A)
_HpnicfRCPSessionId_Type=Integer32
_HpnicfRCPSessionId_Object=MibTableColumn
hpnicfRCPSessionId=_HpnicfRCPSessionId_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,2,3,1,1),_HpnicfRCPSessionId_Type())
hpnicfRCPSessionId.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRCPSessionId.setStatus(_A)
_HpnicfRCPSessionClientIPType_Type=InetAddressType
_HpnicfRCPSessionClientIPType_Object=MibTableColumn
hpnicfRCPSessionClientIPType=_HpnicfRCPSessionClientIPType_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,2,3,1,2),_HpnicfRCPSessionClientIPType_Type())
hpnicfRCPSessionClientIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRCPSessionClientIPType.setStatus(_A)
_HpnicfRCPSessionClientIP_Type=InetAddress
_HpnicfRCPSessionClientIP_Object=MibTableColumn
hpnicfRCPSessionClientIP=_HpnicfRCPSessionClientIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,2,3,1,3),_HpnicfRCPSessionClientIP_Type())
hpnicfRCPSessionClientIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRCPSessionClientIP.setStatus(_A)
class _HpnicfRCPSessionRunningStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('connected',1),('operational',2)))
_HpnicfRCPSessionRunningStatus_Type.__name__=_H
_HpnicfRCPSessionRunningStatus_Object=MibTableColumn
hpnicfRCPSessionRunningStatus=_HpnicfRCPSessionRunningStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,2,3,1,4),_HpnicfRCPSessionRunningStatus_Type())
hpnicfRCPSessionRunningStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRCPSessionRunningStatus.setStatus(_A)
_HpnicfRCPSessionUserName_Type=DisplayString
_HpnicfRCPSessionUserName_Object=MibTableColumn
hpnicfRCPSessionUserName=_HpnicfRCPSessionUserName_Object((1,3,6,1,4,1,11,2,14,11,15,2,73,1,2,3,1,5),_HpnicfRCPSessionUserName_Type())
hpnicfRCPSessionUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRCPSessionUserName.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'hpnicfRCPMIB':hpnicfRCPMIB,'hpnicfRCPLeaf':hpnicfRCPLeaf,'hpnicfRCPServerEnableStatus':hpnicfRCPServerEnableStatus,'hpnicfRCPConnTimeout':hpnicfRCPConnTimeout,'hpnicfRCPRuleTimeout':hpnicfRCPRuleTimeout,'hpnicfRCPServerMaxConn':hpnicfRCPServerMaxConn,'hpnicfRCPServerCurConn':hpnicfRCPServerCurConn,'hpnicfRCPConnTimeoutMaxValue':hpnicfRCPConnTimeoutMaxValue,'hpnicfRCPRuleTimeoutMaxValue':hpnicfRCPRuleTimeoutMaxValue,'hpnicfRCPServerMaxConnMaxValue':hpnicfRCPServerMaxConnMaxValue,'hpnicfRCPBalanceGroupIdMinValue':hpnicfRCPBalanceGroupIdMinValue,'hpnicfRCPBalanceGroupIdMaxValue':hpnicfRCPBalanceGroupIdMaxValue,'hpnicfRCPTotalUsers':hpnicfRCPTotalUsers,'hpnicfRCPTotalClientIPs':hpnicfRCPTotalClientIPs,'hpnicfRCPTable':hpnicfRCPTable,'hpnicfRCPUserTable':hpnicfRCPUserTable,'hpnicfRCPUserEntry':hpnicfRCPUserEntry,_I:hpnicfRCPUserName,'hpnicfRCPUserPassword':hpnicfRCPUserPassword,'hpnicfRCPUserRedirectInterface':hpnicfRCPUserRedirectInterface,'hpnicfRCPUserRedirectBalanceGroup':hpnicfRCPUserRedirectBalanceGroup,'hpnicfRCPUserRowStatus':hpnicfRCPUserRowStatus,'hpnicfRCPClientIPTable':hpnicfRCPClientIPTable,'hpnicfRCPClientIPEntry':hpnicfRCPClientIPEntry,_J:hpnicfRCPClientIPType,_K:hpnicfRCPClientIP,'hpnicfRCPClientIPRowStatus':hpnicfRCPClientIPRowStatus,'hpnicfRCPSessionTable':hpnicfRCPSessionTable,'hpnicfRCPSessionEntry':hpnicfRCPSessionEntry,_L:hpnicfRCPSessionId,'hpnicfRCPSessionClientIPType':hpnicfRCPSessionClientIPType,'hpnicfRCPSessionClientIP':hpnicfRCPSessionClientIP,'hpnicfRCPSessionRunningStatus':hpnicfRCPSessionRunningStatus,'hpnicfRCPSessionUserName':hpnicfRCPSessionUserName})