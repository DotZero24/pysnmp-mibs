_B='current'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cFcoeMode=ModuleIdentity((1,3,6,1,4,1,2011,10,2,135))
if mibBuilder.loadTexts:h3cFcoeMode.setRevisions(('2013-03-08 11:00',))
_H3cFcoeModeMibObjects_ObjectIdentity=ObjectIdentity
h3cFcoeModeMibObjects=_H3cFcoeModeMibObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,135,1))
_H3cFcoeModeCfgMode_Type=Integer32
_H3cFcoeModeCfgMode_Object=MibScalar
h3cFcoeModeCfgMode=_H3cFcoeModeCfgMode_Object((1,3,6,1,4,1,2011,10,2,135,1,1),_H3cFcoeModeCfgMode_Type())
h3cFcoeModeCfgMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:h3cFcoeModeCfgMode.setStatus(_B)
class _H3cFcoeModeCfgLastResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('success',1),('noLicence',2),('needReset',3),('unknownFault',4)))
_H3cFcoeModeCfgLastResult_Type.__name__=_A
_H3cFcoeModeCfgLastResult_Object=MibScalar
h3cFcoeModeCfgLastResult=_H3cFcoeModeCfgLastResult_Object((1,3,6,1,4,1,2011,10,2,135,1,2),_H3cFcoeModeCfgLastResult_Type())
h3cFcoeModeCfgLastResult.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cFcoeModeCfgLastResult.setStatus(_B)
mibBuilder.exportSymbols('H3C-FCOE-MODE-MIB',**{'h3cFcoeMode':h3cFcoeMode,'h3cFcoeModeMibObjects':h3cFcoeModeMibObjects,'h3cFcoeModeCfgMode':h3cFcoeModeCfgMode,'h3cFcoeModeCfgLastResult':h3cFcoeModeCfgLastResult})