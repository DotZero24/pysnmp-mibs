_F='nsAddrIndex'
_E='NETSCREEN-ADDR-MIB'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenAddr,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenAddr')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
netscreenAddrMibModule=ModuleIdentity((1,3,6,1,4,1,3224,12,0))
if mibBuilder.loadTexts:netscreenAddrMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-10 00:00','2001-09-28 00:00','2001-05-14 00:00'))
_NsAddrTable_Object=MibTable
nsAddrTable=_NsAddrTable_Object((1,3,6,1,4,1,3224,12,1))
if mibBuilder.loadTexts:nsAddrTable.setStatus(_A)
_NsAddrEntry_Object=MibTableRow
nsAddrEntry=_NsAddrEntry_Object((1,3,6,1,4,1,3224,12,1,1))
nsAddrEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:nsAddrEntry.setStatus(_A)
class _NsAddrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsAddrIndex_Type.__name__=_D
_NsAddrIndex_Object=MibTableColumn
nsAddrIndex=_NsAddrIndex_Object((1,3,6,1,4,1,3224,12,1,1,1),_NsAddrIndex_Type())
nsAddrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAddrIndex.setStatus(_A)
class _NsAddrName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsAddrName_Type.__name__=_C
_NsAddrName_Object=MibTableColumn
nsAddrName=_NsAddrName_Object((1,3,6,1,4,1,3224,12,1,1,2),_NsAddrName_Type())
nsAddrName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAddrName.setStatus(_A)
_NsAddrVsys_Type=Integer32
_NsAddrVsys_Object=MibTableColumn
nsAddrVsys=_NsAddrVsys_Object((1,3,6,1,4,1,3224,12,1,1,3),_NsAddrVsys_Type())
nsAddrVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAddrVsys.setStatus(_A)
_NsAddrZone_Type=Integer32
_NsAddrZone_Object=MibTableColumn
nsAddrZone=_NsAddrZone_Object((1,3,6,1,4,1,3224,12,1,1,4),_NsAddrZone_Type())
nsAddrZone.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAddrZone.setStatus(_A)
class _NsAddrIpOrDomain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsAddrIpOrDomain_Type.__name__=_C
_NsAddrIpOrDomain_Object=MibTableColumn
nsAddrIpOrDomain=_NsAddrIpOrDomain_Object((1,3,6,1,4,1,3224,12,1,1,5),_NsAddrIpOrDomain_Type())
nsAddrIpOrDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAddrIpOrDomain.setStatus(_A)
_NsAddrNetmask_Type=IpAddress
_NsAddrNetmask_Object=MibTableColumn
nsAddrNetmask=_NsAddrNetmask_Object((1,3,6,1,4,1,3224,12,1,1,6),_NsAddrNetmask_Type())
nsAddrNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAddrNetmask.setStatus(_A)
class _NsAddrComment_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsAddrComment_Type.__name__=_C
_NsAddrComment_Object=MibTableColumn
nsAddrComment=_NsAddrComment_Object((1,3,6,1,4,1,3224,12,1,1,7),_NsAddrComment_Type())
nsAddrComment.setMaxAccess(_B)
if mibBuilder.loadTexts:nsAddrComment.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'netscreenAddrMibModule':netscreenAddrMibModule,'nsAddrTable':nsAddrTable,'nsAddrEntry':nsAddrEntry,_F:nsAddrIndex,'nsAddrName':nsAddrName,'nsAddrVsys':nsAddrVsys,'nsAddrZone':nsAddrZone,'nsAddrIpOrDomain':nsAddrIpOrDomain,'nsAddrNetmask':nsAddrNetmask,'nsAddrComment':nsAddrComment})