_J='radiusSrvProtocol'
_I='BIANCA-BRICK-RADIUS-MIB'
_H='enabled'
_G='disabled'
_F='DisplayString'
_E='read-only'
_D='Counter32'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_D,'Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bintecsec_ObjectIdentity=ObjectIdentity
bintecsec=_Bintecsec_ObjectIdentity((1,3,6,1,4,1,272,254))
_Radius_ObjectIdentity=ObjectIdentity
radius=_Radius_ObjectIdentity((1,3,6,1,4,1,272,254,8))
_RadiusServerTable_Object=MibTable
radiusServerTable=_RadiusServerTable_Object((1,3,6,1,4,1,272,254,8,1))
if mibBuilder.loadTexts:radiusServerTable.setStatus(_A)
_RadiusServerEntry_Object=MibTableRow
radiusServerEntry=_RadiusServerEntry_Object((1,3,6,1,4,1,272,254,8,1,1))
radiusServerEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:radiusServerEntry.setStatus(_A)
class _RadiusSrvProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('authentication',1),('accounting',2),('login',3),('ipsec',4),('wpa802-1x',5),('xauth',6)))
_RadiusSrvProtocol_Type.__name__=_C
_RadiusSrvProtocol_Object=MibTableColumn
radiusSrvProtocol=_RadiusSrvProtocol_Object((1,3,6,1,4,1,272,254,8,1,1,1),_RadiusSrvProtocol_Type())
radiusSrvProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusSrvProtocol.setStatus(_A)
_RadiusSrvAddress_Type=IpAddress
_RadiusSrvAddress_Object=MibTableColumn
radiusSrvAddress=_RadiusSrvAddress_Object((1,3,6,1,4,1,272,254,8,1,1,2),_RadiusSrvAddress_Type())
radiusSrvAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusSrvAddress.setStatus(_A)
class _RadiusSrvPort_Type(Integer32):defaultValue=1812
_RadiusSrvPort_Type.__name__=_C
_RadiusSrvPort_Object=MibTableColumn
radiusSrvPort=_RadiusSrvPort_Object((1,3,6,1,4,1,272,254,8,1,1,3),_RadiusSrvPort_Type())
radiusSrvPort.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusSrvPort.setStatus(_A)
class _RadiusSrvSecret_Type(DisplayString):defaultValue=OctetString('')
_RadiusSrvSecret_Type.__name__=_F
_RadiusSrvSecret_Object=MibTableColumn
radiusSrvSecret=_RadiusSrvSecret_Object((1,3,6,1,4,1,272,254,8,1,1,4),_RadiusSrvSecret_Type())
radiusSrvSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusSrvSecret.setStatus(_A)
class _RadiusSrvPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RadiusSrvPriority_Type.__name__=_C
_RadiusSrvPriority_Object=MibTableColumn
radiusSrvPriority=_RadiusSrvPriority_Object((1,3,6,1,4,1,272,254,8,1,1,5),_RadiusSrvPriority_Type())
radiusSrvPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusSrvPriority.setStatus(_A)
class _RadiusSrvTimeout_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,50000))
_RadiusSrvTimeout_Type.__name__=_C
_RadiusSrvTimeout_Object=MibTableColumn
radiusSrvTimeout=_RadiusSrvTimeout_Object((1,3,6,1,4,1,272,254,8,1,1,6),_RadiusSrvTimeout_Type())
radiusSrvTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusSrvTimeout.setStatus(_A)
class _RadiusSrvRetries_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_RadiusSrvRetries_Type.__name__=_C
_RadiusSrvRetries_Object=MibTableColumn
radiusSrvRetries=_RadiusSrvRetries_Object((1,3,6,1,4,1,272,254,8,1,1,7),_RadiusSrvRetries_Type())
radiusSrvRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusSrvRetries.setStatus(_A)
class _RadiusSrvState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('active',1),('inactive',2),(_G,3),('delete',4)))
_RadiusSrvState_Type.__name__=_C
_RadiusSrvState_Object=MibTableColumn
radiusSrvState=_RadiusSrvState_Object((1,3,6,1,4,1,272,254,8,1,1,8),_RadiusSrvState_Type())
radiusSrvState.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusSrvState.setStatus(_A)
class _RadiusSrvPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('authoritative',1),('non-authoritative',2)))
_RadiusSrvPolicy_Type.__name__=_C
_RadiusSrvPolicy_Object=MibTableColumn
radiusSrvPolicy=_RadiusSrvPolicy_Object((1,3,6,1,4,1,272,254,8,1,1,9),_RadiusSrvPolicy_Type())
radiusSrvPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusSrvPolicy.setStatus(_A)
class _RadiusSrvValidate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_RadiusSrvValidate_Type.__name__=_C
_RadiusSrvValidate_Object=MibTableColumn
radiusSrvValidate=_RadiusSrvValidate_Object((1,3,6,1,4,1,272,254,8,1,1,10),_RadiusSrvValidate_Type())
radiusSrvValidate.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusSrvValidate.setStatus(_A)
class _RadiusSrvDialout_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_G,2),('reload',3)))
_RadiusSrvDialout_Type.__name__=_C
_RadiusSrvDialout_Object=MibTableColumn
radiusSrvDialout=_RadiusSrvDialout_Object((1,3,6,1,4,1,272,254,8,1,1,11),_RadiusSrvDialout_Type())
radiusSrvDialout.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusSrvDialout.setStatus(_A)
class _RadiusSrvDefaultPW_Type(DisplayString):defaultValue=OctetString('')
_RadiusSrvDefaultPW_Type.__name__=_F
_RadiusSrvDefaultPW_Object=MibTableColumn
radiusSrvDefaultPW=_RadiusSrvDefaultPW_Object((1,3,6,1,4,1,272,254,8,1,1,12),_RadiusSrvDefaultPW_Type())
radiusSrvDefaultPW.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusSrvDefaultPW.setStatus(_A)
class _RadiusSrvReloadInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_RadiusSrvReloadInterval_Type.__name__=_C
_RadiusSrvReloadInterval_Object=MibTableColumn
radiusSrvReloadInterval=_RadiusSrvReloadInterval_Object((1,3,6,1,4,1,272,254,8,1,1,13),_RadiusSrvReloadInterval_Type())
radiusSrvReloadInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusSrvReloadInterval.setStatus(_A)
class _RadiusSrvAuthRequests_Type(Counter32):defaultValue=0
_RadiusSrvAuthRequests_Type.__name__=_D
_RadiusSrvAuthRequests_Object=MibTableColumn
radiusSrvAuthRequests=_RadiusSrvAuthRequests_Object((1,3,6,1,4,1,272,254,8,1,1,14),_RadiusSrvAuthRequests_Type())
radiusSrvAuthRequests.setMaxAccess(_E)
if mibBuilder.loadTexts:radiusSrvAuthRequests.setStatus(_A)
class _RadiusSrvAuthAccepts_Type(Counter32):defaultValue=0
_RadiusSrvAuthAccepts_Type.__name__=_D
_RadiusSrvAuthAccepts_Object=MibTableColumn
radiusSrvAuthAccepts=_RadiusSrvAuthAccepts_Object((1,3,6,1,4,1,272,254,8,1,1,15),_RadiusSrvAuthAccepts_Type())
radiusSrvAuthAccepts.setMaxAccess(_E)
if mibBuilder.loadTexts:radiusSrvAuthAccepts.setStatus(_A)
class _RadiusSrvAuthRejects_Type(Counter32):defaultValue=0
_RadiusSrvAuthRejects_Type.__name__=_D
_RadiusSrvAuthRejects_Object=MibTableColumn
radiusSrvAuthRejects=_RadiusSrvAuthRejects_Object((1,3,6,1,4,1,272,254,8,1,1,16),_RadiusSrvAuthRejects_Type())
radiusSrvAuthRejects.setMaxAccess(_E)
if mibBuilder.loadTexts:radiusSrvAuthRejects.setStatus(_A)
class _RadiusSrvAuthReqRetrans_Type(Counter32):defaultValue=0
_RadiusSrvAuthReqRetrans_Type.__name__=_D
_RadiusSrvAuthReqRetrans_Object=MibTableColumn
radiusSrvAuthReqRetrans=_RadiusSrvAuthReqRetrans_Object((1,3,6,1,4,1,272,254,8,1,1,17),_RadiusSrvAuthReqRetrans_Type())
radiusSrvAuthReqRetrans.setMaxAccess(_E)
if mibBuilder.loadTexts:radiusSrvAuthReqRetrans.setStatus(_A)
class _RadiusSrvAuthReqFailed_Type(Counter32):defaultValue=0
_RadiusSrvAuthReqFailed_Type.__name__=_D
_RadiusSrvAuthReqFailed_Object=MibTableColumn
radiusSrvAuthReqFailed=_RadiusSrvAuthReqFailed_Object((1,3,6,1,4,1,272,254,8,1,1,18),_RadiusSrvAuthReqFailed_Type())
radiusSrvAuthReqFailed.setMaxAccess(_E)
if mibBuilder.loadTexts:radiusSrvAuthReqFailed.setStatus(_A)
class _RadiusSrvAuthReqPending_Type(Counter32):defaultValue=0
_RadiusSrvAuthReqPending_Type.__name__=_D
_RadiusSrvAuthReqPending_Object=MibTableColumn
radiusSrvAuthReqPending=_RadiusSrvAuthReqPending_Object((1,3,6,1,4,1,272,254,8,1,1,19),_RadiusSrvAuthReqPending_Type())
radiusSrvAuthReqPending.setMaxAccess(_E)
if mibBuilder.loadTexts:radiusSrvAuthReqPending.setStatus(_A)
class _RadiusSrvAcctStarts_Type(Counter32):defaultValue=0
_RadiusSrvAcctStarts_Type.__name__=_D
_RadiusSrvAcctStarts_Object=MibTableColumn
radiusSrvAcctStarts=_RadiusSrvAcctStarts_Object((1,3,6,1,4,1,272,254,8,1,1,20),_RadiusSrvAcctStarts_Type())
radiusSrvAcctStarts.setMaxAccess(_E)
if mibBuilder.loadTexts:radiusSrvAcctStarts.setStatus(_A)
class _RadiusSrvAcctStops_Type(Counter32):defaultValue=0
_RadiusSrvAcctStops_Type.__name__=_D
_RadiusSrvAcctStops_Object=MibTableColumn
radiusSrvAcctStops=_RadiusSrvAcctStops_Object((1,3,6,1,4,1,272,254,8,1,1,21),_RadiusSrvAcctStops_Type())
radiusSrvAcctStops.setMaxAccess(_E)
if mibBuilder.loadTexts:radiusSrvAcctStops.setStatus(_A)
class _RadiusSrvKeepalive_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_RadiusSrvKeepalive_Type.__name__=_C
_RadiusSrvKeepalive_Object=MibTableColumn
radiusSrvKeepalive=_RadiusSrvKeepalive_Object((1,3,6,1,4,1,272,254,8,1,1,22),_RadiusSrvKeepalive_Type())
radiusSrvKeepalive.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusSrvKeepalive.setStatus(_A)
class _RadiusSrvGroupId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_RadiusSrvGroupId_Type.__name__=_C
_RadiusSrvGroupId_Object=MibTableColumn
radiusSrvGroupId=_RadiusSrvGroupId_Object((1,3,6,1,4,1,272,254,8,1,1,23),_RadiusSrvGroupId_Type())
radiusSrvGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusSrvGroupId.setStatus(_A)
class _RadiusSrvNasLocation_Type(DisplayString):defaultValue=OctetString('')
_RadiusSrvNasLocation_Type.__name__=_F
_RadiusSrvNasLocation_Object=MibTableColumn
radiusSrvNasLocation=_RadiusSrvNasLocation_Object((1,3,6,1,4,1,272,254,8,1,1,24),_RadiusSrvNasLocation_Type())
radiusSrvNasLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusSrvNasLocation.setStatus(_A)
class _RadiusSrvVendorMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('default',1),('emulation-1',2),('emulation-2',3)))
_RadiusSrvVendorMode_Type.__name__=_C
_RadiusSrvVendorMode_Object=MibTableColumn
radiusSrvVendorMode=_RadiusSrvVendorMode_Object((1,3,6,1,4,1,272,254,8,1,1,25),_RadiusSrvVendorMode_Type())
radiusSrvVendorMode.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusSrvVendorMode.setStatus(_A)
class _RadiusSrvAcctOns_Type(Counter32):defaultValue=0
_RadiusSrvAcctOns_Type.__name__=_D
_RadiusSrvAcctOns_Object=MibTableColumn
radiusSrvAcctOns=_RadiusSrvAcctOns_Object((1,3,6,1,4,1,272,254,8,1,1,26),_RadiusSrvAcctOns_Type())
radiusSrvAcctOns.setMaxAccess(_E)
if mibBuilder.loadTexts:radiusSrvAcctOns.setStatus(_A)
class _RadiusSrvAcctOffs_Type(Counter32):defaultValue=0
_RadiusSrvAcctOffs_Type.__name__=_D
_RadiusSrvAcctOffs_Object=MibTableColumn
radiusSrvAcctOffs=_RadiusSrvAcctOffs_Object((1,3,6,1,4,1,272,254,8,1,1,27),_RadiusSrvAcctOffs_Type())
radiusSrvAcctOffs.setMaxAccess(_E)
if mibBuilder.loadTexts:radiusSrvAcctOffs.setStatus(_A)
class _RadiusSrvAcctResponses_Type(Counter32):defaultValue=0
_RadiusSrvAcctResponses_Type.__name__=_D
_RadiusSrvAcctResponses_Object=MibTableColumn
radiusSrvAcctResponses=_RadiusSrvAcctResponses_Object((1,3,6,1,4,1,272,254,8,1,1,28),_RadiusSrvAcctResponses_Type())
radiusSrvAcctResponses.setMaxAccess(_E)
if mibBuilder.loadTexts:radiusSrvAcctResponses.setStatus(_A)
class _RadiusSrvGroupDescr_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RadiusSrvGroupDescr_Type.__name__=_F
_RadiusSrvGroupDescr_Object=MibTableColumn
radiusSrvGroupDescr=_RadiusSrvGroupDescr_Object((1,3,6,1,4,1,272,254,8,1,1,29),_RadiusSrvGroupDescr_Type())
radiusSrvGroupDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusSrvGroupDescr.setStatus(_A)
_RadiusSrvNasOspfAreaId_Type=IpAddress
_RadiusSrvNasOspfAreaId_Object=MibTableColumn
radiusSrvNasOspfAreaId=_RadiusSrvNasOspfAreaId_Object((1,3,6,1,4,1,272,254,8,1,1,30),_RadiusSrvNasOspfAreaId_Type())
radiusSrvNasOspfAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusSrvNasOspfAreaId.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'bintec':bintec,'bintecsec':bintecsec,'radius':radius,'radiusServerTable':radiusServerTable,'radiusServerEntry':radiusServerEntry,_J:radiusSrvProtocol,'radiusSrvAddress':radiusSrvAddress,'radiusSrvPort':radiusSrvPort,'radiusSrvSecret':radiusSrvSecret,'radiusSrvPriority':radiusSrvPriority,'radiusSrvTimeout':radiusSrvTimeout,'radiusSrvRetries':radiusSrvRetries,'radiusSrvState':radiusSrvState,'radiusSrvPolicy':radiusSrvPolicy,'radiusSrvValidate':radiusSrvValidate,'radiusSrvDialout':radiusSrvDialout,'radiusSrvDefaultPW':radiusSrvDefaultPW,'radiusSrvReloadInterval':radiusSrvReloadInterval,'radiusSrvAuthRequests':radiusSrvAuthRequests,'radiusSrvAuthAccepts':radiusSrvAuthAccepts,'radiusSrvAuthRejects':radiusSrvAuthRejects,'radiusSrvAuthReqRetrans':radiusSrvAuthReqRetrans,'radiusSrvAuthReqFailed':radiusSrvAuthReqFailed,'radiusSrvAuthReqPending':radiusSrvAuthReqPending,'radiusSrvAcctStarts':radiusSrvAcctStarts,'radiusSrvAcctStops':radiusSrvAcctStops,'radiusSrvKeepalive':radiusSrvKeepalive,'radiusSrvGroupId':radiusSrvGroupId,'radiusSrvNasLocation':radiusSrvNasLocation,'radiusSrvVendorMode':radiusSrvVendorMode,'radiusSrvAcctOns':radiusSrvAcctOns,'radiusSrvAcctOffs':radiusSrvAcctOffs,'radiusSrvAcctResponses':radiusSrvAcctResponses,'radiusSrvGroupDescr':radiusSrvGroupDescr,'radiusSrvNasOspfAreaId':radiusSrvNasOspfAreaId})