_H='nsVpnIkeIndex'
_G='NETSCREEN-VPN-IKE-MIB'
_F='enabled'
_E='disable'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenVpn,netscreenVpnMibModule=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenVpn','netscreenVpnMibModule')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
netscreenVpnIkeMibModule=ModuleIdentity((1,3,6,1,4,1,3224,4,0,3))
if mibBuilder.loadTexts:netscreenVpnIkeMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-13 00:00','2001-09-28 00:00','2001-05-14 00:00'))
_NsVpnIke_ObjectIdentity=ObjectIdentity
nsVpnIke=_NsVpnIke_ObjectIdentity((1,3,6,1,4,1,3224,4,3))
_NsVpnIkeTable_Object=MibTable
nsVpnIkeTable=_NsVpnIkeTable_Object((1,3,6,1,4,1,3224,4,3,1))
if mibBuilder.loadTexts:nsVpnIkeTable.setStatus(_A)
_NsVpnIkeEntry_Object=MibTableRow
nsVpnIkeEntry=_NsVpnIkeEntry_Object((1,3,6,1,4,1,3224,4,3,1,1))
nsVpnIkeEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:nsVpnIkeEntry.setStatus(_A)
class _NsVpnIkeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsVpnIkeIndex_Type.__name__=_D
_NsVpnIkeIndex_Object=MibTableColumn
nsVpnIkeIndex=_NsVpnIkeIndex_Object((1,3,6,1,4,1,3224,4,3,1,1,1),_NsVpnIkeIndex_Type())
nsVpnIkeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnIkeIndex.setStatus(_A)
class _NsVpnIkeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnIkeName_Type.__name__=_C
_NsVpnIkeName_Object=MibTableColumn
nsVpnIkeName=_NsVpnIkeName_Object((1,3,6,1,4,1,3224,4,3,1,1,2),_NsVpnIkeName_Type())
nsVpnIkeName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnIkeName.setStatus(_A)
class _NsVpnIkeReplayProc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NsVpnIkeReplayProc_Type.__name__=_D
_NsVpnIkeReplayProc_Object=MibTableColumn
nsVpnIkeReplayProc=_NsVpnIkeReplayProc_Object((1,3,6,1,4,1,3224,4,3,1,1,3),_NsVpnIkeReplayProc_Type())
nsVpnIkeReplayProc.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnIkeReplayProc.setStatus(_A)
class _NsVpnIkeGWTun_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnIkeGWTun_Type.__name__=_C
_NsVpnIkeGWTun_Object=MibTableColumn
nsVpnIkeGWTun=_NsVpnIkeGWTun_Object((1,3,6,1,4,1,3224,4,3,1,1,4),_NsVpnIkeGWTun_Type())
nsVpnIkeGWTun.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnIkeGWTun.setStatus(_A)
class _NsVpnIkePh2ProOne_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnIkePh2ProOne_Type.__name__=_C
_NsVpnIkePh2ProOne_Object=MibTableColumn
nsVpnIkePh2ProOne=_NsVpnIkePh2ProOne_Object((1,3,6,1,4,1,3224,4,3,1,1,5),_NsVpnIkePh2ProOne_Type())
nsVpnIkePh2ProOne.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnIkePh2ProOne.setStatus(_A)
class _NsVpnIkePh2ProTwo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnIkePh2ProTwo_Type.__name__=_C
_NsVpnIkePh2ProTwo_Object=MibTableColumn
nsVpnIkePh2ProTwo=_NsVpnIkePh2ProTwo_Object((1,3,6,1,4,1,3224,4,3,1,1,6),_NsVpnIkePh2ProTwo_Type())
nsVpnIkePh2ProTwo.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnIkePh2ProTwo.setStatus(_A)
class _NsVpnIkePh2ProThree_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnIkePh2ProThree_Type.__name__=_C
_NsVpnIkePh2ProThree_Object=MibTableColumn
nsVpnIkePh2ProThree=_NsVpnIkePh2ProThree_Object((1,3,6,1,4,1,3224,4,3,1,1,7),_NsVpnIkePh2ProThree_Type())
nsVpnIkePh2ProThree.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnIkePh2ProThree.setStatus(_A)
class _NsVpnIkePh2ProFour_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnIkePh2ProFour_Type.__name__=_C
_NsVpnIkePh2ProFour_Object=MibTableColumn
nsVpnIkePh2ProFour=_NsVpnIkePh2ProFour_Object((1,3,6,1,4,1,3224,4,3,1,1,8),_NsVpnIkePh2ProFour_Type())
nsVpnIkePh2ProFour.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnIkePh2ProFour.setStatus(_A)
class _NsVpnIkeMonitorEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NsVpnIkeMonitorEnable_Type.__name__=_D
_NsVpnIkeMonitorEnable_Object=MibTableColumn
nsVpnIkeMonitorEnable=_NsVpnIkeMonitorEnable_Object((1,3,6,1,4,1,3224,4,3,1,1,9),_NsVpnIkeMonitorEnable_Type())
nsVpnIkeMonitorEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnIkeMonitorEnable.setStatus(_A)
class _NsVpnIkeTransMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NsVpnIkeTransMode_Type.__name__=_D
_NsVpnIkeTransMode_Object=MibTableColumn
nsVpnIkeTransMode=_NsVpnIkeTransMode_Object((1,3,6,1,4,1,3224,4,3,1,1,10),_NsVpnIkeTransMode_Type())
nsVpnIkeTransMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnIkeTransMode.setStatus(_A)
_NsVpnIkeVsys_Type=Integer32
_NsVpnIkeVsys_Object=MibTableColumn
nsVpnIkeVsys=_NsVpnIkeVsys_Object((1,3,6,1,4,1,3224,4,3,1,1,11),_NsVpnIkeVsys_Type())
nsVpnIkeVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnIkeVsys.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'netscreenVpnIkeMibModule':netscreenVpnIkeMibModule,'nsVpnIke':nsVpnIke,'nsVpnIkeTable':nsVpnIkeTable,'nsVpnIkeEntry':nsVpnIkeEntry,_H:nsVpnIkeIndex,'nsVpnIkeName':nsVpnIkeName,'nsVpnIkeReplayProc':nsVpnIkeReplayProc,'nsVpnIkeGWTun':nsVpnIkeGWTun,'nsVpnIkePh2ProOne':nsVpnIkePh2ProOne,'nsVpnIkePh2ProTwo':nsVpnIkePh2ProTwo,'nsVpnIkePh2ProThree':nsVpnIkePh2ProThree,'nsVpnIkePh2ProFour':nsVpnIkePh2ProFour,'nsVpnIkeMonitorEnable':nsVpnIkeMonitorEnable,'nsVpnIkeTransMode':nsVpnIkeTransMode,'nsVpnIkeVsys':nsVpnIkeVsys})