_E='slRadiusServerIndex'
_D='SL-RADIUS-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
slMain,=mibBuilder.importSymbols('SL-MAIN-MIB','slMain')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
slRadiusMIB=ModuleIdentity((1,3,6,1,4,1,4515,1,3,23))
class SharedSecret(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_SlRadiusClientMIBObjects_ObjectIdentity=ObjectIdentity
slRadiusClientMIBObjects=_SlRadiusClientMIBObjects_ObjectIdentity((1,3,6,1,4,1,4515,1,3,23,1))
_SlRadiusClient_ObjectIdentity=ObjectIdentity
slRadiusClient=_SlRadiusClient_ObjectIdentity((1,3,6,1,4,1,4515,1,3,23,1,1))
_SlRadiusEnabled_Type=TruthValue
_SlRadiusEnabled_Object=MibScalar
slRadiusEnabled=_SlRadiusEnabled_Object((1,3,6,1,4,1,4515,1,3,23,1,1,1),_SlRadiusEnabled_Type())
slRadiusEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:slRadiusEnabled.setStatus(_A)
_SlRadiusServerTable_Object=MibTable
slRadiusServerTable=_SlRadiusServerTable_Object((1,3,6,1,4,1,4515,1,3,23,1,1,2))
if mibBuilder.loadTexts:slRadiusServerTable.setStatus(_A)
_SlRadiusServerEntry_Object=MibTableRow
slRadiusServerEntry=_SlRadiusServerEntry_Object((1,3,6,1,4,1,4515,1,3,23,1,1,2,1))
slRadiusServerEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:slRadiusServerEntry.setStatus(_A)
_SlRadiusServerIndex_Type=Integer32
_SlRadiusServerIndex_Object=MibTableColumn
slRadiusServerIndex=_SlRadiusServerIndex_Object((1,3,6,1,4,1,4515,1,3,23,1,1,2,1,1),_SlRadiusServerIndex_Type())
slRadiusServerIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:slRadiusServerIndex.setStatus(_A)
_SlRadiusServerAddress_Type=IpAddress
_SlRadiusServerAddress_Object=MibTableColumn
slRadiusServerAddress=_SlRadiusServerAddress_Object((1,3,6,1,4,1,4515,1,3,23,1,1,2,1,2),_SlRadiusServerAddress_Type())
slRadiusServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:slRadiusServerAddress.setStatus(_A)
_SlRadiusServerPort_Type=Integer32
_SlRadiusServerPort_Object=MibTableColumn
slRadiusServerPort=_SlRadiusServerPort_Object((1,3,6,1,4,1,4515,1,3,23,1,1,2,1,3),_SlRadiusServerPort_Type())
slRadiusServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slRadiusServerPort.setStatus(_A)
class _SlRadiusServerAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_SlRadiusServerAdminStatus_Type.__name__=_C
_SlRadiusServerAdminStatus_Object=MibTableColumn
slRadiusServerAdminStatus=_SlRadiusServerAdminStatus_Object((1,3,6,1,4,1,4515,1,3,23,1,1,2,1,4),_SlRadiusServerAdminStatus_Type())
slRadiusServerAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:slRadiusServerAdminStatus.setStatus(_A)
_SlRadiusTimeout_Type=Integer32
_SlRadiusTimeout_Object=MibTableColumn
slRadiusTimeout=_SlRadiusTimeout_Object((1,3,6,1,4,1,4515,1,3,23,1,1,2,1,5),_SlRadiusTimeout_Type())
slRadiusTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:slRadiusTimeout.setStatus(_A)
_SlRadiusSharedSecret_Type=SharedSecret
_SlRadiusSharedSecret_Object=MibTableColumn
slRadiusSharedSecret=_SlRadiusSharedSecret_Object((1,3,6,1,4,1,4515,1,3,23,1,1,2,1,6),_SlRadiusSharedSecret_Type())
slRadiusSharedSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:slRadiusSharedSecret.setStatus(_A)
_SlRadiusTraps_ObjectIdentity=ObjectIdentity
slRadiusTraps=_SlRadiusTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,3,23,1,2))
mibBuilder.exportSymbols(_D,**{'SharedSecret':SharedSecret,'slRadiusMIB':slRadiusMIB,'slRadiusClientMIBObjects':slRadiusClientMIBObjects,'slRadiusClient':slRadiusClient,'slRadiusEnabled':slRadiusEnabled,'slRadiusServerTable':slRadiusServerTable,'slRadiusServerEntry':slRadiusServerEntry,_E:slRadiusServerIndex,'slRadiusServerAddress':slRadiusServerAddress,'slRadiusServerPort':slRadiusServerPort,'slRadiusServerAdminStatus':slRadiusServerAdminStatus,'slRadiusTimeout':slRadiusTimeout,'slRadiusSharedSecret':slRadiusSharedSecret,'slRadiusTraps':slRadiusTraps})