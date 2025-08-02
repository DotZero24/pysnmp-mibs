_D='wlsxCtsIndex'
_C='WLSX-CTS-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wlsxEnterpriseMibModules,=mibBuilder.importSymbols('ARUBA-MIB','wlsxEnterpriseMibModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','snmpModules')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TAddress,TDomain,TextualConvention,TestAndIncr,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','StorageType','TAddress','TDomain','TextualConvention','TestAndIncr','TimeInterval','TruthValue')
wlsxCtsMIB=ModuleIdentity((1,3,6,1,4,1,14823,2,2,1,11))
if mibBuilder.loadTexts:wlsxCtsMIB.setRevisions(('2020-08-14 17:45',))
_WlsxCtsOpGroup_ObjectIdentity=ObjectIdentity
wlsxCtsOpGroup=_WlsxCtsOpGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,11,1))
_WlsxCtsRequestTable_Object=MibTable
wlsxCtsRequestTable=_WlsxCtsRequestTable_Object((1,3,6,1,4,1,14823,2,2,1,11,1,1))
if mibBuilder.loadTexts:wlsxCtsRequestTable.setStatus(_A)
_WlsxCtsRequestEntry_Object=MibTableRow
wlsxCtsRequestEntry=_WlsxCtsRequestEntry_Object((1,3,6,1,4,1,14823,2,2,1,11,1,1,1))
wlsxCtsRequestEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:wlsxCtsRequestEntry.setStatus(_A)
_WlsxCtsIndex_Type=Integer32
_WlsxCtsIndex_Object=MibTableColumn
wlsxCtsIndex=_WlsxCtsIndex_Object((1,3,6,1,4,1,14823,2,2,1,11,1,1,1,1),_WlsxCtsIndex_Type())
wlsxCtsIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:wlsxCtsIndex.setStatus(_A)
_WlsxCtsOpcode_Type=DisplayString
_WlsxCtsOpcode_Object=MibTableColumn
wlsxCtsOpcode=_WlsxCtsOpcode_Object((1,3,6,1,4,1,14823,2,2,1,11,1,1,1,2),_WlsxCtsOpcode_Type())
wlsxCtsOpcode.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxCtsOpcode.setStatus(_A)
_WlsxCtsCookie_Type=DisplayString
_WlsxCtsCookie_Object=MibTableColumn
wlsxCtsCookie=_WlsxCtsCookie_Object((1,3,6,1,4,1,14823,2,2,1,11,1,1,1,3),_WlsxCtsCookie_Type())
wlsxCtsCookie.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxCtsCookie.setStatus(_A)
_WlsxCtsURL_Type=DisplayString
_WlsxCtsURL_Object=MibTableColumn
wlsxCtsURL=_WlsxCtsURL_Object((1,3,6,1,4,1,14823,2,2,1,11,1,1,1,4),_WlsxCtsURL_Type())
wlsxCtsURL.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxCtsURL.setStatus(_A)
class _WlsxCtsFlags_Type(Bits):namedValues=NamedValues(*(('wlsxCtsFlagForce',0),('wlsxCtsFlagUseCert',1)))
_WlsxCtsFlags_Type.__name__='Bits'
_WlsxCtsFlags_Object=MibTableColumn
wlsxCtsFlags=_WlsxCtsFlags_Object((1,3,6,1,4,1,14823,2,2,1,11,1,1,1,5),_WlsxCtsFlags_Type())
wlsxCtsFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxCtsFlags.setStatus(_A)
_WlsxCtsStatus_Type=RowStatus
_WlsxCtsStatus_Object=MibTableColumn
wlsxCtsStatus=_WlsxCtsStatus_Object((1,3,6,1,4,1,14823,2,2,1,11,1,1,1,6),_WlsxCtsStatus_Type())
wlsxCtsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxCtsStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'wlsxCtsMIB':wlsxCtsMIB,'wlsxCtsOpGroup':wlsxCtsOpGroup,'wlsxCtsRequestTable':wlsxCtsRequestTable,'wlsxCtsRequestEntry':wlsxCtsRequestEntry,_D:wlsxCtsIndex,'wlsxCtsOpcode':wlsxCtsOpcode,'wlsxCtsCookie':wlsxCtsCookie,'wlsxCtsURL':wlsxCtsURL,'wlsxCtsFlags':wlsxCtsFlags,'wlsxCtsStatus':wlsxCtsStatus})