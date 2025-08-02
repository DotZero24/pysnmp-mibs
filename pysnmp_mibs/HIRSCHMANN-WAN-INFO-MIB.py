_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmWanMgmt,=mibBuilder.importSymbols('HIRSCHMANN-WAN-MIB','hmWanMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hmWanInfoMib=ModuleIdentity((1,3,6,1,4,1,248,40,1,6))
if mibBuilder.loadTexts:hmWanInfoMib.setRevisions(('2016-08-09 00:00',))
_HmWanInfoProduct_Type=DisplayString
_HmWanInfoProduct_Object=MibScalar
hmWanInfoProduct=_HmWanInfoProduct_Object((1,3,6,1,4,1,248,40,1,6,1),_HmWanInfoProduct_Type())
hmWanInfoProduct.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanInfoProduct.setStatus(_B)
_HmWanInfoFirmware_Type=DisplayString
_HmWanInfoFirmware_Object=MibScalar
hmWanInfoFirmware=_HmWanInfoFirmware_Object((1,3,6,1,4,1,248,40,1,6,2),_HmWanInfoFirmware_Type())
hmWanInfoFirmware.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanInfoFirmware.setStatus(_B)
_HmWanInfoSN_Type=DisplayString
_HmWanInfoSN_Object=MibScalar
hmWanInfoSN=_HmWanInfoSN_Object((1,3,6,1,4,1,248,40,1,6,3),_HmWanInfoSN_Type())
hmWanInfoSN.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanInfoSN.setStatus(_B)
_HmWanInfoIMEI_Type=OctetString
_HmWanInfoIMEI_Object=MibScalar
hmWanInfoIMEI=_HmWanInfoIMEI_Object((1,3,6,1,4,1,248,40,1,6,4),_HmWanInfoIMEI_Type())
hmWanInfoIMEI.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanInfoIMEI.setStatus(_B)
_HmWanInfoESN_Type=OctetString
_HmWanInfoESN_Object=MibScalar
hmWanInfoESN=_HmWanInfoESN_Object((1,3,6,1,4,1,248,40,1,6,5),_HmWanInfoESN_Type())
hmWanInfoESN.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanInfoESN.setStatus(_B)
_HmWanInfoMEID_Type=OctetString
_HmWanInfoMEID_Object=MibScalar
hmWanInfoMEID=_HmWanInfoMEID_Object((1,3,6,1,4,1,248,40,1,6,6),_HmWanInfoMEID_Type())
hmWanInfoMEID.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanInfoMEID.setStatus(_B)
_HmWanInfoICCID_Type=OctetString
_HmWanInfoICCID_Object=MibScalar
hmWanInfoICCID=_HmWanInfoICCID_Object((1,3,6,1,4,1,248,40,1,6,7),_HmWanInfoICCID_Type())
hmWanInfoICCID.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanInfoICCID.setStatus(_B)
mibBuilder.exportSymbols('HIRSCHMANN-WAN-INFO-MIB',**{'hmWanInfoMib':hmWanInfoMib,'hmWanInfoProduct':hmWanInfoProduct,'hmWanInfoFirmware':hmWanInfoFirmware,'hmWanInfoSN':hmWanInfoSN,'hmWanInfoIMEI':hmWanInfoIMEI,'hmWanInfoESN':hmWanInfoESN,'hmWanInfoMEID':hmWanInfoMEID,'hmWanInfoICCID':hmWanInfoICCID})