_F='radius'
_E='serverIndex'
_D='G6-RADIUS-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
management=ModuleIdentity((1,3,6,1,4,1,3181,10,6,3))
if mibBuilder.loadTexts:management.setRevisions(('2018-02-12 16:19',))
_Radius_ObjectIdentity=ObjectIdentity
radius=_Radius_ObjectIdentity((1,3,6,1,4,1,3181,10,6,3,69))
_ServerTable_Object=MibTable
serverTable=_ServerTable_Object((1,3,6,1,4,1,3181,10,6,3,69,1))
if mibBuilder.loadTexts:serverTable.setStatus(_A)
_ServerEntry_Object=MibTableRow
serverEntry=_ServerEntry_Object((1,3,6,1,4,1,3181,10,6,3,69,1,1))
serverEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:serverEntry.setStatus(_A)
class _ServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ServerIndex_Type.__name__=_C
_ServerIndex_Object=MibTableColumn
serverIndex=_ServerIndex_Object((1,3,6,1,4,1,3181,10,6,3,69,1,1,1),_ServerIndex_Type())
serverIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:serverIndex.setStatus(_A)
_ServerName_Type=DisplayString
_ServerName_Object=MibTableColumn
serverName=_ServerName_Object((1,3,6,1,4,1,3181,10,6,3,69,1,1,2),_ServerName_Type())
serverName.setMaxAccess(_B)
if mibBuilder.loadTexts:serverName.setStatus(_A)
class _ServerServerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),('tacacs',1)))
_ServerServerType_Type.__name__=_C
_ServerServerType_Object=MibTableColumn
serverServerType=_ServerServerType_Object((1,3,6,1,4,1,3181,10,6,3,69,1,1,3),_ServerServerType_Type())
serverServerType.setMaxAccess(_B)
if mibBuilder.loadTexts:serverServerType.setStatus(_A)
_ServerHostAddress_Type=DisplayString
_ServerHostAddress_Object=MibTableColumn
serverHostAddress=_ServerHostAddress_Object((1,3,6,1,4,1,3181,10,6,3,69,1,1,4),_ServerHostAddress_Type())
serverHostAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:serverHostAddress.setStatus(_A)
class _ServerUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ServerUdpPort_Type.__name__=_C
_ServerUdpPort_Object=MibTableColumn
serverUdpPort=_ServerUdpPort_Object((1,3,6,1,4,1,3181,10,6,3,69,1,1,5),_ServerUdpPort_Type())
serverUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:serverUdpPort.setStatus(_A)
_ServerSharedSecret_Type=DisplayString
_ServerSharedSecret_Object=MibTableColumn
serverSharedSecret=_ServerSharedSecret_Object((1,3,6,1,4,1,3181,10,6,3,69,1,1,6),_ServerSharedSecret_Type())
serverSharedSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:serverSharedSecret.setStatus(_A)
_ServerInterimInterval_Type=Unsigned32
_ServerInterimInterval_Object=MibTableColumn
serverInterimInterval=_ServerInterimInterval_Object((1,3,6,1,4,1,3181,10,6,3,69,1,1,7),_ServerInterimInterval_Type())
serverInterimInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:serverInterimInterval.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'management':management,_F:radius,'serverTable':serverTable,'serverEntry':serverEntry,_E:serverIndex,'serverName':serverName,'serverServerType':serverServerType,'serverHostAddress':serverHostAddress,'serverUdpPort':serverUdpPort,'serverSharedSecret':serverSharedSecret,'serverInterimInterval':serverInterimInterval})