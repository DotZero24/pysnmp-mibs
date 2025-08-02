_J='begemotAtmHWEntry'
_I='BEGEMOT-ATM-MIB'
_H='DisplayString'
_G='ifIndex'
_F='IF-MIB'
_E='unknown'
_D='Integer32'
_C='Unsigned32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
begemot,=mibBuilder.importSymbols('BEGEMOT-MIB','begemot')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
begemotAtm=ModuleIdentity((1,3,6,1,4,1,12325,1,101))
class AtmESI(TextualConvention,OctetString):status=_A;displayHint='1x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_BegemotAtmObjects_ObjectIdentity=ObjectIdentity
begemotAtmObjects=_BegemotAtmObjects_ObjectIdentity((1,3,6,1,4,1,12325,1,101,1))
_BegemotAtmIfTable_Object=MibTable
begemotAtmIfTable=_BegemotAtmIfTable_Object((1,3,6,1,4,1,12325,1,101,1,1))
if mibBuilder.loadTexts:begemotAtmIfTable.setStatus(_A)
_BegemotAtmIfEntry_Object=MibTableRow
begemotAtmIfEntry=_BegemotAtmIfEntry_Object((1,3,6,1,4,1,12325,1,101,1,1,1))
begemotAtmIfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:begemotAtmIfEntry.setStatus(_A)
class _BegemotAtmIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_BegemotAtmIfName_Type.__name__=_H
_BegemotAtmIfName_Object=MibTableColumn
begemotAtmIfName=_BegemotAtmIfName_Object((1,3,6,1,4,1,12325,1,101,1,1,1,1),_BegemotAtmIfName_Type())
begemotAtmIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotAtmIfName.setStatus(_A)
_BegemotAtmIfPcr_Type=Unsigned32
_BegemotAtmIfPcr_Object=MibTableColumn
begemotAtmIfPcr=_BegemotAtmIfPcr_Object((1,3,6,1,4,1,12325,1,101,1,1,1,2),_BegemotAtmIfPcr_Type())
begemotAtmIfPcr.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotAtmIfPcr.setStatus(_A)
class _BegemotAtmIfMedia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('other',1),(_E,3),('utp25',4),('taxi100',5),('taxi140',6),('mm155',7),('sm155',8),('utp155',9),('mm622',10),('sm622',11),('virtual',12)))
_BegemotAtmIfMedia_Type.__name__=_D
_BegemotAtmIfMedia_Object=MibTableColumn
begemotAtmIfMedia=_BegemotAtmIfMedia_Object((1,3,6,1,4,1,12325,1,101,1,1,1,3),_BegemotAtmIfMedia_Type())
begemotAtmIfMedia.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotAtmIfMedia.setStatus(_A)
class _BegemotAtmIfVpiBits_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_BegemotAtmIfVpiBits_Type.__name__=_C
_BegemotAtmIfVpiBits_Object=MibTableColumn
begemotAtmIfVpiBits=_BegemotAtmIfVpiBits_Object((1,3,6,1,4,1,12325,1,101,1,1,1,4),_BegemotAtmIfVpiBits_Type())
begemotAtmIfVpiBits.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotAtmIfVpiBits.setStatus(_A)
class _BegemotAtmIfVciBits_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_BegemotAtmIfVciBits_Type.__name__=_C
_BegemotAtmIfVciBits_Object=MibTableColumn
begemotAtmIfVciBits=_BegemotAtmIfVciBits_Object((1,3,6,1,4,1,12325,1,101,1,1,1,5),_BegemotAtmIfVciBits_Type())
begemotAtmIfVciBits.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotAtmIfVciBits.setStatus(_A)
class _BegemotAtmIfMaxVpcs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_BegemotAtmIfMaxVpcs_Type.__name__=_C
_BegemotAtmIfMaxVpcs_Object=MibTableColumn
begemotAtmIfMaxVpcs=_BegemotAtmIfMaxVpcs_Object((1,3,6,1,4,1,12325,1,101,1,1,1,6),_BegemotAtmIfMaxVpcs_Type())
begemotAtmIfMaxVpcs.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotAtmIfMaxVpcs.setStatus(_A)
class _BegemotAtmIfMaxVccs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777216))
_BegemotAtmIfMaxVccs_Type.__name__=_C
_BegemotAtmIfMaxVccs_Object=MibTableColumn
begemotAtmIfMaxVccs=_BegemotAtmIfMaxVccs_Object((1,3,6,1,4,1,12325,1,101,1,1,1,7),_BegemotAtmIfMaxVccs_Type())
begemotAtmIfMaxVccs.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotAtmIfMaxVccs.setStatus(_A)
_BegemotAtmIfEsi_Type=AtmESI
_BegemotAtmIfEsi_Object=MibTableColumn
begemotAtmIfEsi=_BegemotAtmIfEsi_Object((1,3,6,1,4,1,12325,1,101,1,1,1,8),_BegemotAtmIfEsi_Type())
begemotAtmIfEsi.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotAtmIfEsi.setStatus(_A)
class _BegemotAtmIfCarrierStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('carrierOn',1),('carrierOff',2),(_E,3),('none',4)))
_BegemotAtmIfCarrierStatus_Type.__name__=_D
_BegemotAtmIfCarrierStatus_Object=MibTableColumn
begemotAtmIfCarrierStatus=_BegemotAtmIfCarrierStatus_Object((1,3,6,1,4,1,12325,1,101,1,1,1,9),_BegemotAtmIfCarrierStatus_Type())
begemotAtmIfCarrierStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotAtmIfCarrierStatus.setStatus(_A)
class _BegemotAtmIfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sonet',1),('sdh',2),(_E,3)))
_BegemotAtmIfMode_Type.__name__=_D
_BegemotAtmIfMode_Object=MibTableColumn
begemotAtmIfMode=_BegemotAtmIfMode_Object((1,3,6,1,4,1,12325,1,101,1,1,1,10),_BegemotAtmIfMode_Type())
begemotAtmIfMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:begemotAtmIfMode.setStatus(_A)
_BegemotAtmIfTableLastChange_Type=TimeTicks
_BegemotAtmIfTableLastChange_Object=MibScalar
begemotAtmIfTableLastChange=_BegemotAtmIfTableLastChange_Object((1,3,6,1,4,1,12325,1,101,1,2),_BegemotAtmIfTableLastChange_Type())
begemotAtmIfTableLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotAtmIfTableLastChange.setStatus(_A)
_BegemotAtmHWTable_Object=MibTable
begemotAtmHWTable=_BegemotAtmHWTable_Object((1,3,6,1,4,1,12325,1,101,1,3))
if mibBuilder.loadTexts:begemotAtmHWTable.setStatus(_A)
_BegemotAtmHWEntry_Object=MibTableRow
begemotAtmHWEntry=_BegemotAtmHWEntry_Object((1,3,6,1,4,1,12325,1,101,1,3,1))
if mibBuilder.loadTexts:begemotAtmHWEntry.setStatus(_A)
_BegemotAtmHWVendor_Type=DisplayString
_BegemotAtmHWVendor_Object=MibTableColumn
begemotAtmHWVendor=_BegemotAtmHWVendor_Object((1,3,6,1,4,1,12325,1,101,1,3,1,1),_BegemotAtmHWVendor_Type())
begemotAtmHWVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotAtmHWVendor.setStatus(_A)
_BegemotAtmHWDevice_Type=DisplayString
_BegemotAtmHWDevice_Object=MibTableColumn
begemotAtmHWDevice=_BegemotAtmHWDevice_Object((1,3,6,1,4,1,12325,1,101,1,3,1,2),_BegemotAtmHWDevice_Type())
begemotAtmHWDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotAtmHWDevice.setStatus(_A)
_BegemotAtmHWSerial_Type=Unsigned32
_BegemotAtmHWSerial_Object=MibTableColumn
begemotAtmHWSerial=_BegemotAtmHWSerial_Object((1,3,6,1,4,1,12325,1,101,1,3,1,3),_BegemotAtmHWSerial_Type())
begemotAtmHWSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotAtmHWSerial.setStatus(_A)
_BegemotAtmHWVersion_Type=Unsigned32
_BegemotAtmHWVersion_Object=MibTableColumn
begemotAtmHWVersion=_BegemotAtmHWVersion_Object((1,3,6,1,4,1,12325,1,101,1,3,1,4),_BegemotAtmHWVersion_Type())
begemotAtmHWVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotAtmHWVersion.setStatus(_A)
_BegemotAtmHWSoftVersion_Type=Unsigned32
_BegemotAtmHWSoftVersion_Object=MibTableColumn
begemotAtmHWSoftVersion=_BegemotAtmHWSoftVersion_Object((1,3,6,1,4,1,12325,1,101,1,3,1,5),_BegemotAtmHWSoftVersion_Type())
begemotAtmHWSoftVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotAtmHWSoftVersion.setStatus(_A)
_BegemotAtmSysGroup_ObjectIdentity=ObjectIdentity
begemotAtmSysGroup=_BegemotAtmSysGroup_ObjectIdentity((1,3,6,1,4,1,12325,1,101,1,4))
begemotAtmIfEntry.registerAugmentions((_I,_J))
begemotAtmHWEntry.setIndexNames(*begemotAtmIfEntry.getIndexNames())
mibBuilder.exportSymbols(_I,**{'AtmESI':AtmESI,'begemotAtm':begemotAtm,'begemotAtmObjects':begemotAtmObjects,'begemotAtmIfTable':begemotAtmIfTable,'begemotAtmIfEntry':begemotAtmIfEntry,'begemotAtmIfName':begemotAtmIfName,'begemotAtmIfPcr':begemotAtmIfPcr,'begemotAtmIfMedia':begemotAtmIfMedia,'begemotAtmIfVpiBits':begemotAtmIfVpiBits,'begemotAtmIfVciBits':begemotAtmIfVciBits,'begemotAtmIfMaxVpcs':begemotAtmIfMaxVpcs,'begemotAtmIfMaxVccs':begemotAtmIfMaxVccs,'begemotAtmIfEsi':begemotAtmIfEsi,'begemotAtmIfCarrierStatus':begemotAtmIfCarrierStatus,'begemotAtmIfMode':begemotAtmIfMode,'begemotAtmIfTableLastChange':begemotAtmIfTableLastChange,'begemotAtmHWTable':begemotAtmHWTable,_J:begemotAtmHWEntry,'begemotAtmHWVendor':begemotAtmHWVendor,'begemotAtmHWDevice':begemotAtmHWDevice,'begemotAtmHWSerial':begemotAtmHWSerial,'begemotAtmHWVersion':begemotAtmHWVersion,'begemotAtmHWSoftVersion':begemotAtmHWSoftVersion,'begemotAtmSysGroup':begemotAtmSysGroup})