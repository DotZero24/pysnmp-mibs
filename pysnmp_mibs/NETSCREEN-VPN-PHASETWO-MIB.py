_G='nsVpnPhTwoIndex'
_F='NETSCREEN-VPN-PHASETWO-MIB'
_E='DisplayString'
_D='null'
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
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
netscreenVpnPhasetwoMibModule=ModuleIdentity((1,3,6,1,4,1,3224,4,0,6))
if mibBuilder.loadTexts:netscreenVpnPhasetwoMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-13 00:00','2001-09-28 00:00','2001-05-14 00:00'))
_NsVpnPhaseTwoCfg_ObjectIdentity=ObjectIdentity
nsVpnPhaseTwoCfg=_NsVpnPhaseTwoCfg_ObjectIdentity((1,3,6,1,4,1,3224,4,6))
_NsVpnPhTwoTable_Object=MibTable
nsVpnPhTwoTable=_NsVpnPhTwoTable_Object((1,3,6,1,4,1,3224,4,6,1))
if mibBuilder.loadTexts:nsVpnPhTwoTable.setStatus(_A)
_NsVpnPhTwoEntry_Object=MibTableRow
nsVpnPhTwoEntry=_NsVpnPhTwoEntry_Object((1,3,6,1,4,1,3224,4,6,1,1))
nsVpnPhTwoEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:nsVpnPhTwoEntry.setStatus(_A)
class _NsVpnPhTwoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsVpnPhTwoIndex_Type.__name__=_C
_NsVpnPhTwoIndex_Object=MibTableColumn
nsVpnPhTwoIndex=_NsVpnPhTwoIndex_Object((1,3,6,1,4,1,3224,4,6,1,1,1),_NsVpnPhTwoIndex_Type())
nsVpnPhTwoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnPhTwoIndex.setStatus(_A)
class _NsVpnPhTwoName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnPhTwoName_Type.__name__=_E
_NsVpnPhTwoName_Object=MibTableColumn
nsVpnPhTwoName=_NsVpnPhTwoName_Object((1,3,6,1,4,1,3224,4,6,1,1,2),_NsVpnPhTwoName_Type())
nsVpnPhTwoName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnPhTwoName.setStatus(_A)
_NsVpnPhTwoPFS_Type=Integer32
_NsVpnPhTwoPFS_Object=MibTableColumn
nsVpnPhTwoPFS=_NsVpnPhTwoPFS_Object((1,3,6,1,4,1,3224,4,6,1,1,3),_NsVpnPhTwoPFS_Type())
nsVpnPhTwoPFS.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnPhTwoPFS.setStatus(_A)
class _NsVpnPhTwoEncapMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ah',0),('esp',1)))
_NsVpnPhTwoEncapMethod_Type.__name__=_C
_NsVpnPhTwoEncapMethod_Object=MibTableColumn
nsVpnPhTwoEncapMethod=_NsVpnPhTwoEncapMethod_Object((1,3,6,1,4,1,3224,4,6,1,1,4),_NsVpnPhTwoEncapMethod_Type())
nsVpnPhTwoEncapMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnPhTwoEncapMethod.setStatus(_A)
class _NsVpnPhTwoESPEncryp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_D,0),('des',1),('triple-des',2),('aes',3),('aes-192',4),('aes-256',5)))
_NsVpnPhTwoESPEncryp_Type.__name__=_C
_NsVpnPhTwoESPEncryp_Object=MibTableColumn
nsVpnPhTwoESPEncryp=_NsVpnPhTwoESPEncryp_Object((1,3,6,1,4,1,3224,4,6,1,1,5),_NsVpnPhTwoESPEncryp_Type())
nsVpnPhTwoESPEncryp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnPhTwoESPEncryp.setStatus(_A)
class _NsVpnPhTwoESPAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),('md5',1),('sha',2),('sha-256',3)))
_NsVpnPhTwoESPAuth_Type.__name__=_C
_NsVpnPhTwoESPAuth_Object=MibTableColumn
nsVpnPhTwoESPAuth=_NsVpnPhTwoESPAuth_Object((1,3,6,1,4,1,3224,4,6,1,1,6),_NsVpnPhTwoESPAuth_Type())
nsVpnPhTwoESPAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnPhTwoESPAuth.setStatus(_A)
class _NsVpnPhTwoAhAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('md5',1),('sha',2)))
_NsVpnPhTwoAhAuth_Type.__name__=_C
_NsVpnPhTwoAhAuth_Object=MibTableColumn
nsVpnPhTwoAhAuth=_NsVpnPhTwoAhAuth_Object((1,3,6,1,4,1,3224,4,6,1,1,7),_NsVpnPhTwoAhAuth_Type())
nsVpnPhTwoAhAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnPhTwoAhAuth.setStatus(_A)
_NsVpnPhTwoLifetime_Type=Integer32
_NsVpnPhTwoLifetime_Object=MibTableColumn
nsVpnPhTwoLifetime=_NsVpnPhTwoLifetime_Object((1,3,6,1,4,1,3224,4,6,1,1,8),_NsVpnPhTwoLifetime_Type())
nsVpnPhTwoLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnPhTwoLifetime.setStatus(_A)
class _NsVpnPhTwoLifetimeMeasure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('second',0),('minute',1),('hours',2),('days',3)))
_NsVpnPhTwoLifetimeMeasure_Type.__name__=_C
_NsVpnPhTwoLifetimeMeasure_Object=MibTableColumn
nsVpnPhTwoLifetimeMeasure=_NsVpnPhTwoLifetimeMeasure_Object((1,3,6,1,4,1,3224,4,6,1,1,9),_NsVpnPhTwoLifetimeMeasure_Type())
nsVpnPhTwoLifetimeMeasure.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnPhTwoLifetimeMeasure.setStatus(_A)
_NsVpnPhTwoLifetimeKb_Type=Integer32
_NsVpnPhTwoLifetimeKb_Object=MibTableColumn
nsVpnPhTwoLifetimeKb=_NsVpnPhTwoLifetimeKb_Object((1,3,6,1,4,1,3224,4,6,1,1,10),_NsVpnPhTwoLifetimeKb_Type())
nsVpnPhTwoLifetimeKb.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnPhTwoLifetimeKb.setStatus(_A)
_NsVpnPhTwoVsys_Type=Integer32
_NsVpnPhTwoVsys_Object=MibTableColumn
nsVpnPhTwoVsys=_NsVpnPhTwoVsys_Object((1,3,6,1,4,1,3224,4,6,1,1,11),_NsVpnPhTwoVsys_Type())
nsVpnPhTwoVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnPhTwoVsys.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'netscreenVpnPhasetwoMibModule':netscreenVpnPhasetwoMibModule,'nsVpnPhaseTwoCfg':nsVpnPhaseTwoCfg,'nsVpnPhTwoTable':nsVpnPhTwoTable,'nsVpnPhTwoEntry':nsVpnPhTwoEntry,_G:nsVpnPhTwoIndex,'nsVpnPhTwoName':nsVpnPhTwoName,'nsVpnPhTwoPFS':nsVpnPhTwoPFS,'nsVpnPhTwoEncapMethod':nsVpnPhTwoEncapMethod,'nsVpnPhTwoESPEncryp':nsVpnPhTwoESPEncryp,'nsVpnPhTwoESPAuth':nsVpnPhTwoESPAuth,'nsVpnPhTwoAhAuth':nsVpnPhTwoAhAuth,'nsVpnPhTwoLifetime':nsVpnPhTwoLifetime,'nsVpnPhTwoLifetimeMeasure':nsVpnPhTwoLifetimeMeasure,'nsVpnPhTwoLifetimeKb':nsVpnPhTwoLifetimeKb,'nsVpnPhTwoVsys':nsVpnPhTwoVsys})