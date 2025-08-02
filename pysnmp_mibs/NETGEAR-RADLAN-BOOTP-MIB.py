_G='read-create'
_F='rndBootPActionIfIndex'
_E='NETGEAR-RADLAN-BOOTP-MIB'
_D='read-write'
_C='IpAddress'
_B='SnmpAdminString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
rnd,=mibBuilder.importSymbols('NETGEAR-RADLAN-MIB','rnd')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_B)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32',_C,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
rndBootP=ModuleIdentity((1,3,6,1,4,1,4526,17,24))
if mibBuilder.loadTexts:rndBootP.setRevisions(('2007-01-02 00:00',))
class _RndBootPServerAddress_Type(IpAddress):defaultHexValue='00000000'
_RndBootPServerAddress_Type.__name__=_C
_RndBootPServerAddress_Object=MibScalar
rndBootPServerAddress=_RndBootPServerAddress_Object((1,3,6,1,4,1,4526,17,24,1),_RndBootPServerAddress_Type())
rndBootPServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:rndBootPServerAddress.setStatus(_A)
_RndBootPRelaySecThreshold_Type=Integer32
_RndBootPRelaySecThreshold_Object=MibScalar
rndBootPRelaySecThreshold=_RndBootPRelaySecThreshold_Object((1,3,6,1,4,1,4526,17,24,2),_RndBootPRelaySecThreshold_Type())
rndBootPRelaySecThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:rndBootPRelaySecThreshold.setStatus(_A)
_RndBootPActionTable_Object=MibTable
rndBootPActionTable=_RndBootPActionTable_Object((1,3,6,1,4,1,4526,17,24,3))
if mibBuilder.loadTexts:rndBootPActionTable.setStatus(_A)
_RndBootPActionEntry_Object=MibTableRow
rndBootPActionEntry=_RndBootPActionEntry_Object((1,3,6,1,4,1,4526,17,24,3,1))
rndBootPActionEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:rndBootPActionEntry.setStatus(_A)
_RndBootPActionIfIndex_Type=InterfaceIndex
_RndBootPActionIfIndex_Object=MibTableColumn
rndBootPActionIfIndex=_RndBootPActionIfIndex_Object((1,3,6,1,4,1,4526,17,24,3,1,1),_RndBootPActionIfIndex_Type())
rndBootPActionIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:rndBootPActionIfIndex.setStatus(_A)
_RndBootPActionStatus_Type=RowStatus
_RndBootPActionStatus_Object=MibTableColumn
rndBootPActionStatus=_RndBootPActionStatus_Object((1,3,6,1,4,1,4526,17,24,3,1,2),_RndBootPActionStatus_Type())
rndBootPActionStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rndBootPActionStatus.setStatus(_A)
class _RndBootPActionHostName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RndBootPActionHostName_Type.__name__=_B
_RndBootPActionHostName_Object=MibTableColumn
rndBootPActionHostName=_RndBootPActionHostName_Object((1,3,6,1,4,1,4526,17,24,3,1,3),_RndBootPActionHostName_Type())
rndBootPActionHostName.setMaxAccess(_G)
if mibBuilder.loadTexts:rndBootPActionHostName.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'rndBootP':rndBootP,'rndBootPServerAddress':rndBootPServerAddress,'rndBootPRelaySecThreshold':rndBootPRelaySecThreshold,'rndBootPActionTable':rndBootPActionTable,'rndBootPActionEntry':rndBootPActionEntry,_F:rndBootPActionIfIndex,'rndBootPActionStatus':rndBootPActionStatus,'rndBootPActionHostName':rndBootPActionHostName})