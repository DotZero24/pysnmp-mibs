_B='mandatory'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_LanOptics_ObjectIdentity=ObjectIdentity
lanOptics=_LanOptics_ObjectIdentity((1,3,6,1,4,1,224))
_LanOpticsBridgeProxyAgent_ObjectIdentity=ObjectIdentity
lanOpticsBridgeProxyAgent=_LanOpticsBridgeProxyAgent_ObjectIdentity((1,3,6,1,4,1,224,6))
_LanOpticsLMGRAgent_ObjectIdentity=ObjectIdentity
lanOpticsLMGRAgent=_LanOpticsLMGRAgent_ObjectIdentity((1,3,6,1,4,1,224,6,8))
class _LanOpticsLMGRLinkID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_LanOpticsLMGRLinkID_Type.__name__=_A
_LanOpticsLMGRLinkID_Object=MibScalar
lanOpticsLMGRLinkID=_LanOpticsLMGRLinkID_Object((1,3,6,1,4,1,224,6,8,1),_LanOpticsLMGRLinkID_Type())
lanOpticsLMGRLinkID.setMaxAccess('read-only')
if mibBuilder.loadTexts:lanOpticsLMGRLinkID.setStatus(_B)
class _LanOpticsLMGRCaptCntrlLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('enabled',1))
_LanOpticsLMGRCaptCntrlLink_Type.__name__=_A
_LanOpticsLMGRCaptCntrlLink_Object=MibScalar
lanOpticsLMGRCaptCntrlLink=_LanOpticsLMGRCaptCntrlLink_Object((1,3,6,1,4,1,224,6,8,2),_LanOpticsLMGRCaptCntrlLink_Type())
lanOpticsLMGRCaptCntrlLink.setMaxAccess('read-write')
if mibBuilder.loadTexts:lanOpticsLMGRCaptCntrlLink.setStatus(_B)
mibBuilder.exportSymbols('LANOPTICS-BRIDGE-OPTION-MIB',**{'lanOptics':lanOptics,'lanOpticsBridgeProxyAgent':lanOpticsBridgeProxyAgent,'lanOpticsLMGRAgent':lanOpticsLMGRAgent,'lanOpticsLMGRLinkID':lanOpticsLMGRLinkID,'lanOpticsLMGRCaptCntrlLink':lanOpticsLMGRCaptCntrlLink})