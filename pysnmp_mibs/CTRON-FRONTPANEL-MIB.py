_F='ctFpRedundAddrId'
_E='CTRON-FRONTPANEL-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctFpRedundancy,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctFpRedundancy')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtFpRedund_ObjectIdentity=ObjectIdentity
ctFpRedund=_CtFpRedund_ObjectIdentity((1,3,6,1,4,1,52,4,1,5,5,1))
class _CtFpRedundReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noReset',1),('reset',2)))
_CtFpRedundReset_Type.__name__=_C
_CtFpRedundReset_Object=MibScalar
ctFpRedundReset=_CtFpRedundReset_Object((1,3,6,1,4,1,52,4,1,5,5,1,1),_CtFpRedundReset_Type())
ctFpRedundReset.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFpRedundReset.setStatus(_A)
_CtFpRedundPollInterval_Type=Integer32
_CtFpRedundPollInterval_Object=MibScalar
ctFpRedundPollInterval=_CtFpRedundPollInterval_Object((1,3,6,1,4,1,52,4,1,5,5,1,2),_CtFpRedundPollInterval_Type())
ctFpRedundPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFpRedundPollInterval.setStatus(_A)
_CtFpRedundRetrys_Type=Integer32
_CtFpRedundRetrys_Object=MibScalar
ctFpRedundRetrys=_CtFpRedundRetrys_Object((1,3,6,1,4,1,52,4,1,5,5,1,3),_CtFpRedundRetrys_Type())
ctFpRedundRetrys.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFpRedundRetrys.setStatus(_A)
_CtFpRedundNumAddr_Type=Integer32
_CtFpRedundNumAddr_Object=MibScalar
ctFpRedundNumAddr=_CtFpRedundNumAddr_Object((1,3,6,1,4,1,52,4,1,5,5,1,4),_CtFpRedundNumAddr_Type())
ctFpRedundNumAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ctFpRedundNumAddr.setStatus(_A)
_CtFpRedundAddAddr_Type=IpAddress
_CtFpRedundAddAddr_Object=MibScalar
ctFpRedundAddAddr=_CtFpRedundAddAddr_Object((1,3,6,1,4,1,52,4,1,5,5,1,5),_CtFpRedundAddAddr_Type())
ctFpRedundAddAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFpRedundAddAddr.setStatus(_A)
_CtFpRedundDelAddr_Type=IpAddress
_CtFpRedundDelAddr_Object=MibScalar
ctFpRedundDelAddr=_CtFpRedundDelAddr_Object((1,3,6,1,4,1,52,4,1,5,5,1,6),_CtFpRedundDelAddr_Type())
ctFpRedundDelAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFpRedundDelAddr.setStatus(_A)
_CtFpRedundActivePort_Type=Integer32
_CtFpRedundActivePort_Object=MibScalar
ctFpRedundActivePort=_CtFpRedundActivePort_Object((1,3,6,1,4,1,52,4,1,5,5,1,7),_CtFpRedundActivePort_Type())
ctFpRedundActivePort.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFpRedundActivePort.setStatus(_A)
class _CtFpRedundEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_CtFpRedundEnable_Type.__name__=_C
_CtFpRedundEnable_Object=MibScalar
ctFpRedundEnable=_CtFpRedundEnable_Object((1,3,6,1,4,1,52,4,1,5,5,1,8),_CtFpRedundEnable_Type())
ctFpRedundEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFpRedundEnable.setStatus(_A)
_CtFpRedundAddrTable_Object=MibTable
ctFpRedundAddrTable=_CtFpRedundAddrTable_Object((1,3,6,1,4,1,52,4,1,5,5,1,9))
if mibBuilder.loadTexts:ctFpRedundAddrTable.setStatus(_A)
_CtFpRedundAddrEntry_Object=MibTableRow
ctFpRedundAddrEntry=_CtFpRedundAddrEntry_Object((1,3,6,1,4,1,52,4,1,5,5,1,9,1))
ctFpRedundAddrEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ctFpRedundAddrEntry.setStatus(_A)
class _CtFpRedundAddrId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtFpRedundAddrId_Type.__name__=_C
_CtFpRedundAddrId_Object=MibTableColumn
ctFpRedundAddrId=_CtFpRedundAddrId_Object((1,3,6,1,4,1,52,4,1,5,5,1,9,1,1),_CtFpRedundAddrId_Type())
ctFpRedundAddrId.setMaxAccess(_D)
if mibBuilder.loadTexts:ctFpRedundAddrId.setStatus(_A)
_CtFpRedundAddrIPAddr_Type=IpAddress
_CtFpRedundAddrIPAddr_Object=MibTableColumn
ctFpRedundAddrIPAddr=_CtFpRedundAddrIPAddr_Object((1,3,6,1,4,1,52,4,1,5,5,1,9,1,2),_CtFpRedundAddrIPAddr_Type())
ctFpRedundAddrIPAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ctFpRedundAddrIPAddr.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ctFpRedund':ctFpRedund,'ctFpRedundReset':ctFpRedundReset,'ctFpRedundPollInterval':ctFpRedundPollInterval,'ctFpRedundRetrys':ctFpRedundRetrys,'ctFpRedundNumAddr':ctFpRedundNumAddr,'ctFpRedundAddAddr':ctFpRedundAddAddr,'ctFpRedundDelAddr':ctFpRedundDelAddr,'ctFpRedundActivePort':ctFpRedundActivePort,'ctFpRedundEnable':ctFpRedundEnable,'ctFpRedundAddrTable':ctFpRedundAddrTable,'ctFpRedundAddrEntry':ctFpRedundAddrEntry,_F:ctFpRedundAddrId,'ctFpRedundAddrIPAddr':ctFpRedundAddrIPAddr})