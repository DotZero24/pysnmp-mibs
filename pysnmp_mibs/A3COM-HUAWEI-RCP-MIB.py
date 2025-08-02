_L='h3cRCPSessionId'
_K='h3cRCPClientIP'
_J='h3cRCPClientIPType'
_I='h3cRCPUserName'
_H='Integer32'
_G='DisplayString'
_F='not-accessible'
_E='read-write'
_D='read-create'
_C='A3COM-HUAWEI-RCP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cRCP,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cRCP')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention','TruthValue')
h3cRCPMIB=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,73,1))
if mibBuilder.loadTexts:h3cRCPMIB.setRevisions(('2006-09-20 00:00',))
_H3cRCPLeaf_ObjectIdentity=ObjectIdentity
h3cRCPLeaf=_H3cRCPLeaf_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,73,1,1))
_H3cRCPServerEnableStatus_Type=TruthValue
_H3cRCPServerEnableStatus_Object=MibScalar
h3cRCPServerEnableStatus=_H3cRCPServerEnableStatus_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,1,1),_H3cRCPServerEnableStatus_Type())
h3cRCPServerEnableStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRCPServerEnableStatus.setStatus(_A)
_H3cRCPConnTimeout_Type=Integer32
_H3cRCPConnTimeout_Object=MibScalar
h3cRCPConnTimeout=_H3cRCPConnTimeout_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,1,2),_H3cRCPConnTimeout_Type())
h3cRCPConnTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRCPConnTimeout.setStatus(_A)
_H3cRCPRuleTimeout_Type=Integer32
_H3cRCPRuleTimeout_Object=MibScalar
h3cRCPRuleTimeout=_H3cRCPRuleTimeout_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,1,3),_H3cRCPRuleTimeout_Type())
h3cRCPRuleTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRCPRuleTimeout.setStatus(_A)
_H3cRCPServerMaxConn_Type=Integer32
_H3cRCPServerMaxConn_Object=MibScalar
h3cRCPServerMaxConn=_H3cRCPServerMaxConn_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,1,4),_H3cRCPServerMaxConn_Type())
h3cRCPServerMaxConn.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRCPServerMaxConn.setStatus(_A)
_H3cRCPServerCurConn_Type=Integer32
_H3cRCPServerCurConn_Object=MibScalar
h3cRCPServerCurConn=_H3cRCPServerCurConn_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,1,5),_H3cRCPServerCurConn_Type())
h3cRCPServerCurConn.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRCPServerCurConn.setStatus(_A)
_H3cRCPConnTimeoutMaxValue_Type=Integer32
_H3cRCPConnTimeoutMaxValue_Object=MibScalar
h3cRCPConnTimeoutMaxValue=_H3cRCPConnTimeoutMaxValue_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,1,6),_H3cRCPConnTimeoutMaxValue_Type())
h3cRCPConnTimeoutMaxValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRCPConnTimeoutMaxValue.setStatus(_A)
_H3cRCPRuleTimeoutMaxValue_Type=Integer32
_H3cRCPRuleTimeoutMaxValue_Object=MibScalar
h3cRCPRuleTimeoutMaxValue=_H3cRCPRuleTimeoutMaxValue_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,1,7),_H3cRCPRuleTimeoutMaxValue_Type())
h3cRCPRuleTimeoutMaxValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRCPRuleTimeoutMaxValue.setStatus(_A)
_H3cRCPServerMaxConnMaxValue_Type=Integer32
_H3cRCPServerMaxConnMaxValue_Object=MibScalar
h3cRCPServerMaxConnMaxValue=_H3cRCPServerMaxConnMaxValue_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,1,8),_H3cRCPServerMaxConnMaxValue_Type())
h3cRCPServerMaxConnMaxValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRCPServerMaxConnMaxValue.setStatus(_A)
_H3cRCPBalanceGroupIdMinValue_Type=Integer32
_H3cRCPBalanceGroupIdMinValue_Object=MibScalar
h3cRCPBalanceGroupIdMinValue=_H3cRCPBalanceGroupIdMinValue_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,1,9),_H3cRCPBalanceGroupIdMinValue_Type())
h3cRCPBalanceGroupIdMinValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRCPBalanceGroupIdMinValue.setStatus(_A)
_H3cRCPBalanceGroupIdMaxValue_Type=Integer32
_H3cRCPBalanceGroupIdMaxValue_Object=MibScalar
h3cRCPBalanceGroupIdMaxValue=_H3cRCPBalanceGroupIdMaxValue_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,1,10),_H3cRCPBalanceGroupIdMaxValue_Type())
h3cRCPBalanceGroupIdMaxValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRCPBalanceGroupIdMaxValue.setStatus(_A)
_H3cRCPTotalUsers_Type=Integer32
_H3cRCPTotalUsers_Object=MibScalar
h3cRCPTotalUsers=_H3cRCPTotalUsers_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,1,11),_H3cRCPTotalUsers_Type())
h3cRCPTotalUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRCPTotalUsers.setStatus(_A)
_H3cRCPTotalClientIPs_Type=Integer32
_H3cRCPTotalClientIPs_Object=MibScalar
h3cRCPTotalClientIPs=_H3cRCPTotalClientIPs_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,1,12),_H3cRCPTotalClientIPs_Type())
h3cRCPTotalClientIPs.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRCPTotalClientIPs.setStatus(_A)
_H3cRCPTable_ObjectIdentity=ObjectIdentity
h3cRCPTable=_H3cRCPTable_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,73,1,2))
_H3cRCPUserTable_Object=MibTable
h3cRCPUserTable=_H3cRCPUserTable_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,2,1))
if mibBuilder.loadTexts:h3cRCPUserTable.setStatus(_A)
_H3cRCPUserEntry_Object=MibTableRow
h3cRCPUserEntry=_H3cRCPUserEntry_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,2,1,1))
h3cRCPUserEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:h3cRCPUserEntry.setStatus(_A)
class _H3cRCPUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_H3cRCPUserName_Type.__name__=_G
_H3cRCPUserName_Object=MibTableColumn
h3cRCPUserName=_H3cRCPUserName_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,2,1,1,1),_H3cRCPUserName_Type())
h3cRCPUserName.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cRCPUserName.setStatus(_A)
class _H3cRCPUserPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_H3cRCPUserPassword_Type.__name__=_G
_H3cRCPUserPassword_Object=MibTableColumn
h3cRCPUserPassword=_H3cRCPUserPassword_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,2,1,1,2),_H3cRCPUserPassword_Type())
h3cRCPUserPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRCPUserPassword.setStatus(_A)
_H3cRCPUserRedirectInterface_Type=InterfaceIndexOrZero
_H3cRCPUserRedirectInterface_Object=MibTableColumn
h3cRCPUserRedirectInterface=_H3cRCPUserRedirectInterface_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,2,1,1,3),_H3cRCPUserRedirectInterface_Type())
h3cRCPUserRedirectInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRCPUserRedirectInterface.setStatus(_A)
_H3cRCPUserRedirectBalanceGroup_Type=Integer32
_H3cRCPUserRedirectBalanceGroup_Object=MibTableColumn
h3cRCPUserRedirectBalanceGroup=_H3cRCPUserRedirectBalanceGroup_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,2,1,1,4),_H3cRCPUserRedirectBalanceGroup_Type())
h3cRCPUserRedirectBalanceGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRCPUserRedirectBalanceGroup.setStatus(_A)
_H3cRCPUserRowStatus_Type=RowStatus
_H3cRCPUserRowStatus_Object=MibTableColumn
h3cRCPUserRowStatus=_H3cRCPUserRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,2,1,1,5),_H3cRCPUserRowStatus_Type())
h3cRCPUserRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRCPUserRowStatus.setStatus(_A)
_H3cRCPClientIPTable_Object=MibTable
h3cRCPClientIPTable=_H3cRCPClientIPTable_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,2,2))
if mibBuilder.loadTexts:h3cRCPClientIPTable.setStatus(_A)
_H3cRCPClientIPEntry_Object=MibTableRow
h3cRCPClientIPEntry=_H3cRCPClientIPEntry_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,2,2,1))
h3cRCPClientIPEntry.setIndexNames((0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:h3cRCPClientIPEntry.setStatus(_A)
_H3cRCPClientIPType_Type=InetAddressType
_H3cRCPClientIPType_Object=MibTableColumn
h3cRCPClientIPType=_H3cRCPClientIPType_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,2,2,1,1),_H3cRCPClientIPType_Type())
h3cRCPClientIPType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cRCPClientIPType.setStatus(_A)
_H3cRCPClientIP_Type=InetAddress
_H3cRCPClientIP_Object=MibTableColumn
h3cRCPClientIP=_H3cRCPClientIP_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,2,2,1,2),_H3cRCPClientIP_Type())
h3cRCPClientIP.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cRCPClientIP.setStatus(_A)
_H3cRCPClientIPRowStatus_Type=RowStatus
_H3cRCPClientIPRowStatus_Object=MibTableColumn
h3cRCPClientIPRowStatus=_H3cRCPClientIPRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,2,2,1,3),_H3cRCPClientIPRowStatus_Type())
h3cRCPClientIPRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRCPClientIPRowStatus.setStatus(_A)
_H3cRCPSessionTable_Object=MibTable
h3cRCPSessionTable=_H3cRCPSessionTable_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,2,3))
if mibBuilder.loadTexts:h3cRCPSessionTable.setStatus(_A)
_H3cRCPSessionEntry_Object=MibTableRow
h3cRCPSessionEntry=_H3cRCPSessionEntry_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,2,3,1))
h3cRCPSessionEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:h3cRCPSessionEntry.setStatus(_A)
_H3cRCPSessionId_Type=Integer32
_H3cRCPSessionId_Object=MibTableColumn
h3cRCPSessionId=_H3cRCPSessionId_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,2,3,1,1),_H3cRCPSessionId_Type())
h3cRCPSessionId.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cRCPSessionId.setStatus(_A)
_H3cRCPSessionClientIPType_Type=InetAddressType
_H3cRCPSessionClientIPType_Object=MibTableColumn
h3cRCPSessionClientIPType=_H3cRCPSessionClientIPType_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,2,3,1,2),_H3cRCPSessionClientIPType_Type())
h3cRCPSessionClientIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRCPSessionClientIPType.setStatus(_A)
_H3cRCPSessionClientIP_Type=InetAddress
_H3cRCPSessionClientIP_Object=MibTableColumn
h3cRCPSessionClientIP=_H3cRCPSessionClientIP_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,2,3,1,3),_H3cRCPSessionClientIP_Type())
h3cRCPSessionClientIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRCPSessionClientIP.setStatus(_A)
class _H3cRCPSessionRunningStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('connected',1),('operational',2)))
_H3cRCPSessionRunningStatus_Type.__name__=_H
_H3cRCPSessionRunningStatus_Object=MibTableColumn
h3cRCPSessionRunningStatus=_H3cRCPSessionRunningStatus_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,2,3,1,4),_H3cRCPSessionRunningStatus_Type())
h3cRCPSessionRunningStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRCPSessionRunningStatus.setStatus(_A)
_H3cRCPSessionUserName_Type=DisplayString
_H3cRCPSessionUserName_Object=MibTableColumn
h3cRCPSessionUserName=_H3cRCPSessionUserName_Object((1,3,6,1,4,1,43,45,1,10,2,73,1,2,3,1,5),_H3cRCPSessionUserName_Type())
h3cRCPSessionUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRCPSessionUserName.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'h3cRCPMIB':h3cRCPMIB,'h3cRCPLeaf':h3cRCPLeaf,'h3cRCPServerEnableStatus':h3cRCPServerEnableStatus,'h3cRCPConnTimeout':h3cRCPConnTimeout,'h3cRCPRuleTimeout':h3cRCPRuleTimeout,'h3cRCPServerMaxConn':h3cRCPServerMaxConn,'h3cRCPServerCurConn':h3cRCPServerCurConn,'h3cRCPConnTimeoutMaxValue':h3cRCPConnTimeoutMaxValue,'h3cRCPRuleTimeoutMaxValue':h3cRCPRuleTimeoutMaxValue,'h3cRCPServerMaxConnMaxValue':h3cRCPServerMaxConnMaxValue,'h3cRCPBalanceGroupIdMinValue':h3cRCPBalanceGroupIdMinValue,'h3cRCPBalanceGroupIdMaxValue':h3cRCPBalanceGroupIdMaxValue,'h3cRCPTotalUsers':h3cRCPTotalUsers,'h3cRCPTotalClientIPs':h3cRCPTotalClientIPs,'h3cRCPTable':h3cRCPTable,'h3cRCPUserTable':h3cRCPUserTable,'h3cRCPUserEntry':h3cRCPUserEntry,_I:h3cRCPUserName,'h3cRCPUserPassword':h3cRCPUserPassword,'h3cRCPUserRedirectInterface':h3cRCPUserRedirectInterface,'h3cRCPUserRedirectBalanceGroup':h3cRCPUserRedirectBalanceGroup,'h3cRCPUserRowStatus':h3cRCPUserRowStatus,'h3cRCPClientIPTable':h3cRCPClientIPTable,'h3cRCPClientIPEntry':h3cRCPClientIPEntry,_J:h3cRCPClientIPType,_K:h3cRCPClientIP,'h3cRCPClientIPRowStatus':h3cRCPClientIPRowStatus,'h3cRCPSessionTable':h3cRCPSessionTable,'h3cRCPSessionEntry':h3cRCPSessionEntry,_L:h3cRCPSessionId,'h3cRCPSessionClientIPType':h3cRCPSessionClientIPType,'h3cRCPSessionClientIP':h3cRCPSessionClientIP,'h3cRCPSessionRunningStatus':h3cRCPSessionRunningStatus,'h3cRCPSessionUserName':h3cRCPSessionUserName})