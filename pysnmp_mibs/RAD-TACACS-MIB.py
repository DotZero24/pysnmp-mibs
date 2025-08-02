_M='tacplusStatsEntry'
_L='tacplusServerGroupId'
_K='RadTacacsKeyString'
_J='tacplusServerPort'
_I='tacplusServerAddress'
_H='tacplusServerAddressType'
_G='Integer32'
_F='not-accessible'
_E='RAD-TACACS-MIB'
_D='Unsigned32'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
radSecurity,=mibBuilder.importSymbols('RAD-SMI-MIB','radSecurity')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
radTacacsPlus=ModuleIdentity((1,3,6,1,4,1,164,6,1,14,1))
class RadTacacsKeyString(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TacplusAuthServerTable_Object=MibTable
tacplusAuthServerTable=_TacplusAuthServerTable_Object((1,3,6,1,4,1,164,6,1,14,1,1))
if mibBuilder.loadTexts:tacplusAuthServerTable.setStatus(_A)
_TacplusAuthServerEntry_Object=MibTableRow
tacplusAuthServerEntry=_TacplusAuthServerEntry_Object((1,3,6,1,4,1,164,6,1,14,1,1,1))
tacplusAuthServerEntry.setIndexNames((0,_E,_H),(0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:tacplusAuthServerEntry.setStatus(_A)
_TacplusServerAddressType_Type=InetAddressType
_TacplusServerAddressType_Object=MibTableColumn
tacplusServerAddressType=_TacplusServerAddressType_Object((1,3,6,1,4,1,164,6,1,14,1,1,1,1),_TacplusServerAddressType_Type())
tacplusServerAddressType.setMaxAccess(_F)
if mibBuilder.loadTexts:tacplusServerAddressType.setStatus(_A)
_TacplusServerAddress_Type=InetAddress
_TacplusServerAddress_Object=MibTableColumn
tacplusServerAddress=_TacplusServerAddress_Object((1,3,6,1,4,1,164,6,1,14,1,1,1,2),_TacplusServerAddress_Type())
tacplusServerAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:tacplusServerAddress.setStatus(_A)
class _TacplusServerPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TacplusServerPort_Type.__name__=_D
_TacplusServerPort_Object=MibTableColumn
tacplusServerPort=_TacplusServerPort_Object((1,3,6,1,4,1,164,6,1,14,1,1,1,3),_TacplusServerPort_Type())
tacplusServerPort.setMaxAccess(_F)
if mibBuilder.loadTexts:tacplusServerPort.setStatus(_A)
_TacplusRowStatus_Type=RowStatus
_TacplusRowStatus_Object=MibTableColumn
tacplusRowStatus=_TacplusRowStatus_Object((1,3,6,1,4,1,164,6,1,14,1,1,1,4),_TacplusRowStatus_Type())
tacplusRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tacplusRowStatus.setStatus(_A)
class _TacplusSecretKey_Type(RadTacacsKeyString):defaultValue=OctetString('')
_TacplusSecretKey_Type.__name__=_K
_TacplusSecretKey_Object=MibTableColumn
tacplusSecretKey=_TacplusSecretKey_Object((1,3,6,1,4,1,164,6,1,14,1,1,1,6),_TacplusSecretKey_Type())
tacplusSecretKey.setMaxAccess(_B)
if mibBuilder.loadTexts:tacplusSecretKey.setStatus(_A)
class _TacplusRetryCount_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_TacplusRetryCount_Type.__name__=_D
_TacplusRetryCount_Object=MibTableColumn
tacplusRetryCount=_TacplusRetryCount_Object((1,3,6,1,4,1,164,6,1,14,1,1,1,7),_TacplusRetryCount_Type())
tacplusRetryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tacplusRetryCount.setStatus(_A)
class _TacplusTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TacplusTimeout_Type.__name__=_D
_TacplusTimeout_Object=MibTableColumn
tacplusTimeout=_TacplusTimeout_Object((1,3,6,1,4,1,164,6,1,14,1,1,1,8),_TacplusTimeout_Type())
tacplusTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:tacplusTimeout.setStatus(_A)
class _TacplusAuthentStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('authenticated',1),('authenticationFailure',2),('unknownFailure',3),('idle',4)))
_TacplusAuthentStatus_Type.__name__=_G
_TacplusAuthentStatus_Object=MibTableColumn
tacplusAuthentStatus=_TacplusAuthentStatus_Object((1,3,6,1,4,1,164,6,1,14,1,1,1,9),_TacplusAuthentStatus_Type())
tacplusAuthentStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tacplusAuthentStatus.setStatus(_A)
class _TacplusAccountingPort_Type(Unsigned32):defaultValue=49;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TacplusAccountingPort_Type.__name__=_D
_TacplusAccountingPort_Object=MibTableColumn
tacplusAccountingPort=_TacplusAccountingPort_Object((1,3,6,1,4,1,164,6,1,14,1,1,1,11),_TacplusAccountingPort_Type())
tacplusAccountingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tacplusAccountingPort.setStatus(_A)
class _TacplusServerGroup_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TacplusServerGroup_Type.__name__=_D
_TacplusServerGroup_Object=MibTableColumn
tacplusServerGroup=_TacplusServerGroup_Object((1,3,6,1,4,1,164,6,1,14,1,1,1,12),_TacplusServerGroup_Type())
tacplusServerGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:tacplusServerGroup.setStatus(_A)
class _TacplusAuthenticationPort_Type(Unsigned32):defaultValue=49;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TacplusAuthenticationPort_Type.__name__=_D
_TacplusAuthenticationPort_Object=MibTableColumn
tacplusAuthenticationPort=_TacplusAuthenticationPort_Object((1,3,6,1,4,1,164,6,1,14,1,1,1,13),_TacplusAuthenticationPort_Type())
tacplusAuthenticationPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tacplusAuthenticationPort.setStatus(_A)
_TacplusStatsTable_Object=MibTable
tacplusStatsTable=_TacplusStatsTable_Object((1,3,6,1,4,1,164,6,1,14,1,2))
if mibBuilder.loadTexts:tacplusStatsTable.setStatus(_A)
_TacplusStatsEntry_Object=MibTableRow
tacplusStatsEntry=_TacplusStatsEntry_Object((1,3,6,1,4,1,164,6,1,14,1,2,1))
if mibBuilder.loadTexts:tacplusStatsEntry.setStatus(_A)
class _TacplusClearStaticsCmd_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_TacplusClearStaticsCmd_Type.__name__=_G
_TacplusClearStaticsCmd_Object=MibTableColumn
tacplusClearStaticsCmd=_TacplusClearStaticsCmd_Object((1,3,6,1,4,1,164,6,1,14,1,2,1,1),_TacplusClearStaticsCmd_Type())
tacplusClearStaticsCmd.setMaxAccess('read-write')
if mibBuilder.loadTexts:tacplusClearStaticsCmd.setStatus(_A)
_TacplusAuthRequests_Type=Counter32
_TacplusAuthRequests_Object=MibTableColumn
tacplusAuthRequests=_TacplusAuthRequests_Object((1,3,6,1,4,1,164,6,1,14,1,2,1,2),_TacplusAuthRequests_Type())
tacplusAuthRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:tacplusAuthRequests.setStatus(_A)
_TacplusAuthenRequestTimeouts_Type=Counter32
_TacplusAuthenRequestTimeouts_Object=MibTableColumn
tacplusAuthenRequestTimeouts=_TacplusAuthenRequestTimeouts_Object((1,3,6,1,4,1,164,6,1,14,1,2,1,3),_TacplusAuthenRequestTimeouts_Type())
tacplusAuthenRequestTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:tacplusAuthenRequestTimeouts.setStatus(_A)
_TacplusAuthenUnexpectedResponses_Type=Counter32
_TacplusAuthenUnexpectedResponses_Object=MibTableColumn
tacplusAuthenUnexpectedResponses=_TacplusAuthenUnexpectedResponses_Object((1,3,6,1,4,1,164,6,1,14,1,2,1,4),_TacplusAuthenUnexpectedResponses_Type())
tacplusAuthenUnexpectedResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:tacplusAuthenUnexpectedResponses.setStatus(_A)
_TacplusAuthenServerErrorResponses_Type=Counter32
_TacplusAuthenServerErrorResponses_Object=MibTableColumn
tacplusAuthenServerErrorResponses=_TacplusAuthenServerErrorResponses_Object((1,3,6,1,4,1,164,6,1,14,1,2,1,5),_TacplusAuthenServerErrorResponses_Type())
tacplusAuthenServerErrorResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:tacplusAuthenServerErrorResponses.setStatus(_A)
_TacplusAuthenIncorrectResponses_Type=Counter32
_TacplusAuthenIncorrectResponses_Object=MibTableColumn
tacplusAuthenIncorrectResponses=_TacplusAuthenIncorrectResponses_Object((1,3,6,1,4,1,164,6,1,14,1,2,1,6),_TacplusAuthenIncorrectResponses_Type())
tacplusAuthenIncorrectResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:tacplusAuthenIncorrectResponses.setStatus(_A)
_TacplusAuthenTransactionSuccesses_Type=Counter32
_TacplusAuthenTransactionSuccesses_Object=MibTableColumn
tacplusAuthenTransactionSuccesses=_TacplusAuthenTransactionSuccesses_Object((1,3,6,1,4,1,164,6,1,14,1,2,1,7),_TacplusAuthenTransactionSuccesses_Type())
tacplusAuthenTransactionSuccesses.setMaxAccess(_C)
if mibBuilder.loadTexts:tacplusAuthenTransactionSuccesses.setStatus(_A)
_TacplusAuthenTransactionFailures_Type=Counter32
_TacplusAuthenTransactionFailures_Object=MibTableColumn
tacplusAuthenTransactionFailures=_TacplusAuthenTransactionFailures_Object((1,3,6,1,4,1,164,6,1,14,1,2,1,8),_TacplusAuthenTransactionFailures_Type())
tacplusAuthenTransactionFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:tacplusAuthenTransactionFailures.setStatus(_A)
_TacplusAuthenPendingRequests_Type=Counter32
_TacplusAuthenPendingRequests_Object=MibTableColumn
tacplusAuthenPendingRequests=_TacplusAuthenPendingRequests_Object((1,3,6,1,4,1,164,6,1,14,1,2,1,9),_TacplusAuthenPendingRequests_Type())
tacplusAuthenPendingRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:tacplusAuthenPendingRequests.setStatus(_A)
_TacplusServerGroupTable_Object=MibTable
tacplusServerGroupTable=_TacplusServerGroupTable_Object((1,3,6,1,4,1,164,6,1,14,1,3))
if mibBuilder.loadTexts:tacplusServerGroupTable.setStatus(_A)
_TacplusServerGroupEntry_Object=MibTableRow
tacplusServerGroupEntry=_TacplusServerGroupEntry_Object((1,3,6,1,4,1,164,6,1,14,1,3,1))
tacplusServerGroupEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:tacplusServerGroupEntry.setStatus(_A)
_TacplusServerGroupId_Type=Unsigned32
_TacplusServerGroupId_Object=MibTableColumn
tacplusServerGroupId=_TacplusServerGroupId_Object((1,3,6,1,4,1,164,6,1,14,1,3,1,1),_TacplusServerGroupId_Type())
tacplusServerGroupId.setMaxAccess(_F)
if mibBuilder.loadTexts:tacplusServerGroupId.setStatus(_A)
_TacplusServerGroupRowStatus_Type=RowStatus
_TacplusServerGroupRowStatus_Object=MibTableColumn
tacplusServerGroupRowStatus=_TacplusServerGroupRowStatus_Object((1,3,6,1,4,1,164,6,1,14,1,3,1,2),_TacplusServerGroupRowStatus_Type())
tacplusServerGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tacplusServerGroupRowStatus.setStatus(_A)
_TacplusServerGroupName_Type=SnmpAdminString
_TacplusServerGroupName_Object=MibTableColumn
tacplusServerGroupName=_TacplusServerGroupName_Object((1,3,6,1,4,1,164,6,1,14,1,3,1,3),_TacplusServerGroupName_Type())
tacplusServerGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:tacplusServerGroupName.setStatus(_A)
class _TacplusServerGroupAccountingMode_Type(Bits):namedValues=NamedValues(*(('shell',0),('system',1),('commands',2)))
_TacplusServerGroupAccountingMode_Type.__name__='Bits'
_TacplusServerGroupAccountingMode_Object=MibTableColumn
tacplusServerGroupAccountingMode=_TacplusServerGroupAccountingMode_Object((1,3,6,1,4,1,164,6,1,14,1,3,1,4),_TacplusServerGroupAccountingMode_Type())
tacplusServerGroupAccountingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tacplusServerGroupAccountingMode.setStatus(_A)
tacplusAuthServerEntry.registerAugmentions((_E,_M))
tacplusStatsEntry.setIndexNames(*tacplusAuthServerEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{_K:RadTacacsKeyString,'radTacacsPlus':radTacacsPlus,'tacplusAuthServerTable':tacplusAuthServerTable,'tacplusAuthServerEntry':tacplusAuthServerEntry,_H:tacplusServerAddressType,_I:tacplusServerAddress,_J:tacplusServerPort,'tacplusRowStatus':tacplusRowStatus,'tacplusSecretKey':tacplusSecretKey,'tacplusRetryCount':tacplusRetryCount,'tacplusTimeout':tacplusTimeout,'tacplusAuthentStatus':tacplusAuthentStatus,'tacplusAccountingPort':tacplusAccountingPort,'tacplusServerGroup':tacplusServerGroup,'tacplusAuthenticationPort':tacplusAuthenticationPort,'tacplusStatsTable':tacplusStatsTable,_M:tacplusStatsEntry,'tacplusClearStaticsCmd':tacplusClearStaticsCmd,'tacplusAuthRequests':tacplusAuthRequests,'tacplusAuthenRequestTimeouts':tacplusAuthenRequestTimeouts,'tacplusAuthenUnexpectedResponses':tacplusAuthenUnexpectedResponses,'tacplusAuthenServerErrorResponses':tacplusAuthenServerErrorResponses,'tacplusAuthenIncorrectResponses':tacplusAuthenIncorrectResponses,'tacplusAuthenTransactionSuccesses':tacplusAuthenTransactionSuccesses,'tacplusAuthenTransactionFailures':tacplusAuthenTransactionFailures,'tacplusAuthenPendingRequests':tacplusAuthenPendingRequests,'tacplusServerGroupTable':tacplusServerGroupTable,'tacplusServerGroupEntry':tacplusServerGroupEntry,_L:tacplusServerGroupId,'tacplusServerGroupRowStatus':tacplusServerGroupRowStatus,'tacplusServerGroupName':tacplusServerGroupName,'tacplusServerGroupAccountingMode':tacplusServerGroupAccountingMode})