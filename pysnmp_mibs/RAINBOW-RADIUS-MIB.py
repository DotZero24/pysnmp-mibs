_L='rbRadiusAcctServerAddress'
_K='noAction'
_J='standby'
_I='active'
_H='secondary'
_G='primary'
_F='rbRadiusAuthServerAddress'
_E='RAINBOW-RADIUS-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rainbow,=mibBuilder.importSymbols('RAINBOW-MIB','rainbow')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
rbRadiusClient=ModuleIdentity((1,3,6,1,4,1,12394,1,2,150))
if mibBuilder.loadTexts:rbRadiusClient.setRevisions(('2006-06-06 15:00',))
_RbRadiusClientGeneralParams_ObjectIdentity=ObjectIdentity
rbRadiusClientGeneralParams=_RbRadiusClientGeneralParams_ObjectIdentity((1,3,6,1,4,1,12394,1,2,150,1))
class _RbRadiusClientRetryInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_RbRadiusClientRetryInterval_Type.__name__=_B
_RbRadiusClientRetryInterval_Object=MibScalar
rbRadiusClientRetryInterval=_RbRadiusClientRetryInterval_Object((1,3,6,1,4,1,12394,1,2,150,1,2),_RbRadiusClientRetryInterval_Type())
rbRadiusClientRetryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rbRadiusClientRetryInterval.setStatus(_A)
class _RbRadiusClientMaxNumOfRetries_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_RbRadiusClientMaxNumOfRetries_Type.__name__=_B
_RbRadiusClientMaxNumOfRetries_Object=MibScalar
rbRadiusClientMaxNumOfRetries=_RbRadiusClientMaxNumOfRetries_Object((1,3,6,1,4,1,12394,1,2,150,1,3),_RbRadiusClientMaxNumOfRetries_Type())
rbRadiusClientMaxNumOfRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:rbRadiusClientMaxNumOfRetries.setStatus(_A)
class _RbRadiusClientKeepAliveTimeout_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,180))
_RbRadiusClientKeepAliveTimeout_Type.__name__=_B
_RbRadiusClientKeepAliveTimeout_Object=MibScalar
rbRadiusClientKeepAliveTimeout=_RbRadiusClientKeepAliveTimeout_Object((1,3,6,1,4,1,12394,1,2,150,1,4),_RbRadiusClientKeepAliveTimeout_Type())
rbRadiusClientKeepAliveTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:rbRadiusClientKeepAliveTimeout.setStatus(_A)
_RbRadiusAuthServerTable_Object=MibTable
rbRadiusAuthServerTable=_RbRadiusAuthServerTable_Object((1,3,6,1,4,1,12394,1,2,150,2))
if mibBuilder.loadTexts:rbRadiusAuthServerTable.setStatus(_A)
_RbRadiusAuthServerEntry_Object=MibTableRow
rbRadiusAuthServerEntry=_RbRadiusAuthServerEntry_Object((1,3,6,1,4,1,12394,1,2,150,2,1))
rbRadiusAuthServerEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:rbRadiusAuthServerEntry.setStatus(_A)
_RbRadiusAuthServerAddress_Type=IpAddress
_RbRadiusAuthServerAddress_Object=MibTableColumn
rbRadiusAuthServerAddress=_RbRadiusAuthServerAddress_Object((1,3,6,1,4,1,12394,1,2,150,2,1,1),_RbRadiusAuthServerAddress_Type())
rbRadiusAuthServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:rbRadiusAuthServerAddress.setStatus(_A)
_RbRadiusAuthServerRowStatus_Type=RowStatus
_RbRadiusAuthServerRowStatus_Object=MibTableColumn
rbRadiusAuthServerRowStatus=_RbRadiusAuthServerRowStatus_Object((1,3,6,1,4,1,12394,1,2,150,2,1,2),_RbRadiusAuthServerRowStatus_Type())
rbRadiusAuthServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rbRadiusAuthServerRowStatus.setStatus(_A)
class _RbRadiusAuthServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_RbRadiusAuthServerIndex_Type.__name__=_B
_RbRadiusAuthServerIndex_Object=MibTableColumn
rbRadiusAuthServerIndex=_RbRadiusAuthServerIndex_Object((1,3,6,1,4,1,12394,1,2,150,2,1,3),_RbRadiusAuthServerIndex_Type())
rbRadiusAuthServerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rbRadiusAuthServerIndex.setStatus(_A)
class _RbRadiusAuthServerPortNumber_Type(Integer32):defaultValue=1812;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RbRadiusAuthServerPortNumber_Type.__name__=_B
_RbRadiusAuthServerPortNumber_Object=MibTableColumn
rbRadiusAuthServerPortNumber=_RbRadiusAuthServerPortNumber_Object((1,3,6,1,4,1,12394,1,2,150,2,1,4),_RbRadiusAuthServerPortNumber_Type())
rbRadiusAuthServerPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:rbRadiusAuthServerPortNumber.setStatus(_A)
class _RbRadiusAuthServerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_RbRadiusAuthServerType_Type.__name__=_B
_RbRadiusAuthServerType_Object=MibTableColumn
rbRadiusAuthServerType=_RbRadiusAuthServerType_Object((1,3,6,1,4,1,12394,1,2,150,2,1,5),_RbRadiusAuthServerType_Type())
rbRadiusAuthServerType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbRadiusAuthServerType.setStatus(_A)
class _RbRadiusAuthServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_RbRadiusAuthServerStatus_Type.__name__=_B
_RbRadiusAuthServerStatus_Object=MibTableColumn
rbRadiusAuthServerStatus=_RbRadiusAuthServerStatus_Object((1,3,6,1,4,1,12394,1,2,150,2,1,6),_RbRadiusAuthServerStatus_Type())
rbRadiusAuthServerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rbRadiusAuthServerStatus.setStatus(_A)
class _RbRadiusAuthServerOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_RbRadiusAuthServerOperStatus_Type.__name__=_B
_RbRadiusAuthServerOperStatus_Object=MibTableColumn
rbRadiusAuthServerOperStatus=_RbRadiusAuthServerOperStatus_Object((1,3,6,1,4,1,12394,1,2,150,2,1,7),_RbRadiusAuthServerOperStatus_Type())
rbRadiusAuthServerOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rbRadiusAuthServerOperStatus.setStatus(_A)
class _RbRadiusAuthServerResetCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),('reset',1)))
_RbRadiusAuthServerResetCounters_Type.__name__=_B
_RbRadiusAuthServerResetCounters_Object=MibTableColumn
rbRadiusAuthServerResetCounters=_RbRadiusAuthServerResetCounters_Object((1,3,6,1,4,1,12394,1,2,150,2,1,8),_RbRadiusAuthServerResetCounters_Type())
rbRadiusAuthServerResetCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:rbRadiusAuthServerResetCounters.setStatus(_A)
_RbRadiusAccountServerTable_Object=MibTable
rbRadiusAccountServerTable=_RbRadiusAccountServerTable_Object((1,3,6,1,4,1,12394,1,2,150,3))
if mibBuilder.loadTexts:rbRadiusAccountServerTable.setStatus(_A)
_RbRadiusAccountServerEntry_Object=MibTableRow
rbRadiusAccountServerEntry=_RbRadiusAccountServerEntry_Object((1,3,6,1,4,1,12394,1,2,150,3,1))
rbRadiusAccountServerEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:rbRadiusAccountServerEntry.setStatus(_A)
_RbRadiusAcctServerAddress_Type=IpAddress
_RbRadiusAcctServerAddress_Object=MibTableColumn
rbRadiusAcctServerAddress=_RbRadiusAcctServerAddress_Object((1,3,6,1,4,1,12394,1,2,150,3,1,1),_RbRadiusAcctServerAddress_Type())
rbRadiusAcctServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:rbRadiusAcctServerAddress.setStatus(_A)
_RbRadiusAcctServerRowStatus_Type=RowStatus
_RbRadiusAcctServerRowStatus_Object=MibTableColumn
rbRadiusAcctServerRowStatus=_RbRadiusAcctServerRowStatus_Object((1,3,6,1,4,1,12394,1,2,150,3,1,2),_RbRadiusAcctServerRowStatus_Type())
rbRadiusAcctServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rbRadiusAcctServerRowStatus.setStatus(_A)
class _RbRadiusAcctServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_RbRadiusAcctServerIndex_Type.__name__=_B
_RbRadiusAcctServerIndex_Object=MibTableColumn
rbRadiusAcctServerIndex=_RbRadiusAcctServerIndex_Object((1,3,6,1,4,1,12394,1,2,150,3,1,3),_RbRadiusAcctServerIndex_Type())
rbRadiusAcctServerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rbRadiusAcctServerIndex.setStatus(_A)
class _RbRadiusAcctServerPortNumber_Type(Integer32):defaultValue=1813;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RbRadiusAcctServerPortNumber_Type.__name__=_B
_RbRadiusAcctServerPortNumber_Object=MibTableColumn
rbRadiusAcctServerPortNumber=_RbRadiusAcctServerPortNumber_Object((1,3,6,1,4,1,12394,1,2,150,3,1,4),_RbRadiusAcctServerPortNumber_Type())
rbRadiusAcctServerPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:rbRadiusAcctServerPortNumber.setStatus(_A)
class _RbRadiusAcctServerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_RbRadiusAcctServerType_Type.__name__=_B
_RbRadiusAcctServerType_Object=MibTableColumn
rbRadiusAcctServerType=_RbRadiusAcctServerType_Object((1,3,6,1,4,1,12394,1,2,150,3,1,5),_RbRadiusAcctServerType_Type())
rbRadiusAcctServerType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbRadiusAcctServerType.setStatus(_A)
class _RbRadiusAcctServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_RbRadiusAcctServerStatus_Type.__name__=_B
_RbRadiusAcctServerStatus_Object=MibTableColumn
rbRadiusAcctServerStatus=_RbRadiusAcctServerStatus_Object((1,3,6,1,4,1,12394,1,2,150,3,1,6),_RbRadiusAcctServerStatus_Type())
rbRadiusAcctServerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rbRadiusAcctServerStatus.setStatus(_A)
class _RbRadiusAcctServerOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_RbRadiusAcctServerOperStatus_Type.__name__=_B
_RbRadiusAcctServerOperStatus_Object=MibTableColumn
rbRadiusAcctServerOperStatus=_RbRadiusAcctServerOperStatus_Object((1,3,6,1,4,1,12394,1,2,150,3,1,7),_RbRadiusAcctServerOperStatus_Type())
rbRadiusAcctServerOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rbRadiusAcctServerOperStatus.setStatus(_A)
class _RbRadiusAcctServerResetCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),('reset',1)))
_RbRadiusAcctServerResetCounters_Type.__name__=_B
_RbRadiusAcctServerResetCounters_Object=MibTableColumn
rbRadiusAcctServerResetCounters=_RbRadiusAcctServerResetCounters_Object((1,3,6,1,4,1,12394,1,2,150,3,1,8),_RbRadiusAcctServerResetCounters_Type())
rbRadiusAcctServerResetCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:rbRadiusAcctServerResetCounters.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'rbRadiusClient':rbRadiusClient,'rbRadiusClientGeneralParams':rbRadiusClientGeneralParams,'rbRadiusClientRetryInterval':rbRadiusClientRetryInterval,'rbRadiusClientMaxNumOfRetries':rbRadiusClientMaxNumOfRetries,'rbRadiusClientKeepAliveTimeout':rbRadiusClientKeepAliveTimeout,'rbRadiusAuthServerTable':rbRadiusAuthServerTable,'rbRadiusAuthServerEntry':rbRadiusAuthServerEntry,_F:rbRadiusAuthServerAddress,'rbRadiusAuthServerRowStatus':rbRadiusAuthServerRowStatus,'rbRadiusAuthServerIndex':rbRadiusAuthServerIndex,'rbRadiusAuthServerPortNumber':rbRadiusAuthServerPortNumber,'rbRadiusAuthServerType':rbRadiusAuthServerType,'rbRadiusAuthServerStatus':rbRadiusAuthServerStatus,'rbRadiusAuthServerOperStatus':rbRadiusAuthServerOperStatus,'rbRadiusAuthServerResetCounters':rbRadiusAuthServerResetCounters,'rbRadiusAccountServerTable':rbRadiusAccountServerTable,'rbRadiusAccountServerEntry':rbRadiusAccountServerEntry,_L:rbRadiusAcctServerAddress,'rbRadiusAcctServerRowStatus':rbRadiusAcctServerRowStatus,'rbRadiusAcctServerIndex':rbRadiusAcctServerIndex,'rbRadiusAcctServerPortNumber':rbRadiusAcctServerPortNumber,'rbRadiusAcctServerType':rbRadiusAcctServerType,'rbRadiusAcctServerStatus':rbRadiusAcctServerStatus,'rbRadiusAcctServerOperStatus':rbRadiusAcctServerOperStatus,'rbRadiusAcctServerResetCounters':rbRadiusAcctServerResetCounters})