_F='nsVpnPhOneIndex'
_E='NETSCREEN-VPN-PHASEONE-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenVpn,netscreenVpnMibModule=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenVpn','netscreenVpnMibModule')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
netscreenVpnPhaseoneMibModule=ModuleIdentity((1,3,6,1,4,1,3224,4,0,5))
if mibBuilder.loadTexts:netscreenVpnPhaseoneMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-13 00:00','2001-09-28 00:00','2001-05-14 00:00'))
_NsVpnPhaseOneCfg_ObjectIdentity=ObjectIdentity
nsVpnPhaseOneCfg=_NsVpnPhaseOneCfg_ObjectIdentity((1,3,6,1,4,1,3224,4,5))
_NsVpnPhOneTable_Object=MibTable
nsVpnPhOneTable=_NsVpnPhOneTable_Object((1,3,6,1,4,1,3224,4,5,1))
if mibBuilder.loadTexts:nsVpnPhOneTable.setStatus(_A)
_NsVpnPhOneEntry_Object=MibTableRow
nsVpnPhOneEntry=_NsVpnPhOneEntry_Object((1,3,6,1,4,1,3224,4,5,1,1))
nsVpnPhOneEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:nsVpnPhOneEntry.setStatus(_A)
class _NsVpnPhOneIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsVpnPhOneIndex_Type.__name__=_C
_NsVpnPhOneIndex_Object=MibTableColumn
nsVpnPhOneIndex=_NsVpnPhOneIndex_Object((1,3,6,1,4,1,3224,4,5,1,1,1),_NsVpnPhOneIndex_Type())
nsVpnPhOneIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnPhOneIndex.setStatus(_A)
class _NsVpnPhOneName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnPhOneName_Type.__name__=_D
_NsVpnPhOneName_Object=MibTableColumn
nsVpnPhOneName=_NsVpnPhOneName_Object((1,3,6,1,4,1,3224,4,5,1,1,2),_NsVpnPhOneName_Type())
nsVpnPhOneName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnPhOneName.setStatus(_A)
class _NsVpnPhOneAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('preshare',0),('rsa-sig',1),('dsa-sig',2),('rsa-enc',3),('rsa-rev',4)))
_NsVpnPhOneAuthMethod_Type.__name__=_C
_NsVpnPhOneAuthMethod_Object=MibTableColumn
nsVpnPhOneAuthMethod=_NsVpnPhOneAuthMethod_Object((1,3,6,1,4,1,3224,4,5,1,1,3),_NsVpnPhOneAuthMethod_Type())
nsVpnPhOneAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnPhOneAuthMethod.setStatus(_A)
_NsVpnPhOneDhGroup_Type=Integer32
_NsVpnPhOneDhGroup_Object=MibTableColumn
nsVpnPhOneDhGroup=_NsVpnPhOneDhGroup_Object((1,3,6,1,4,1,3224,4,5,1,1,4),_NsVpnPhOneDhGroup_Type())
nsVpnPhOneDhGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnPhOneDhGroup.setStatus(_A)
class _NsVpnPhOneEncryp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('null',0),('des',1),('des3',2),('aes',3),('aes-192',4),('aes-256',5)))
_NsVpnPhOneEncryp_Type.__name__=_C
_NsVpnPhOneEncryp_Object=MibTableColumn
nsVpnPhOneEncryp=_NsVpnPhOneEncryp_Object((1,3,6,1,4,1,3224,4,5,1,1,5),_NsVpnPhOneEncryp_Type())
nsVpnPhOneEncryp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnPhOneEncryp.setStatus(_A)
class _NsVpnPhOneHash_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('null',0),('md5',1),('sha',2)))
_NsVpnPhOneHash_Type.__name__=_C
_NsVpnPhOneHash_Object=MibTableColumn
nsVpnPhOneHash=_NsVpnPhOneHash_Object((1,3,6,1,4,1,3224,4,5,1,1,6),_NsVpnPhOneHash_Type())
nsVpnPhOneHash.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnPhOneHash.setStatus(_A)
_NsVpnPhOneLifetime_Type=Integer32
_NsVpnPhOneLifetime_Object=MibTableColumn
nsVpnPhOneLifetime=_NsVpnPhOneLifetime_Object((1,3,6,1,4,1,3224,4,5,1,1,7),_NsVpnPhOneLifetime_Type())
nsVpnPhOneLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnPhOneLifetime.setStatus(_A)
class _NsVpnPhOneLifetimeMeasure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('second',0),('minute',1),('hours',2),('days',3)))
_NsVpnPhOneLifetimeMeasure_Type.__name__=_C
_NsVpnPhOneLifetimeMeasure_Object=MibTableColumn
nsVpnPhOneLifetimeMeasure=_NsVpnPhOneLifetimeMeasure_Object((1,3,6,1,4,1,3224,4,5,1,1,8),_NsVpnPhOneLifetimeMeasure_Type())
nsVpnPhOneLifetimeMeasure.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnPhOneLifetimeMeasure.setStatus(_A)
_NsVpnPhOneVsys_Type=Integer32
_NsVpnPhOneVsys_Object=MibTableColumn
nsVpnPhOneVsys=_NsVpnPhOneVsys_Object((1,3,6,1,4,1,3224,4,5,1,1,9),_NsVpnPhOneVsys_Type())
nsVpnPhOneVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnPhOneVsys.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'netscreenVpnPhaseoneMibModule':netscreenVpnPhaseoneMibModule,'nsVpnPhaseOneCfg':nsVpnPhaseOneCfg,'nsVpnPhOneTable':nsVpnPhOneTable,'nsVpnPhOneEntry':nsVpnPhOneEntry,_F:nsVpnPhOneIndex,'nsVpnPhOneName':nsVpnPhOneName,'nsVpnPhOneAuthMethod':nsVpnPhOneAuthMethod,'nsVpnPhOneDhGroup':nsVpnPhOneDhGroup,'nsVpnPhOneEncryp':nsVpnPhOneEncryp,'nsVpnPhOneHash':nsVpnPhOneHash,'nsVpnPhOneLifetime':nsVpnPhOneLifetime,'nsVpnPhOneLifetimeMeasure':nsVpnPhOneLifetimeMeasure,'nsVpnPhOneVsys':nsVpnPhOneVsys})