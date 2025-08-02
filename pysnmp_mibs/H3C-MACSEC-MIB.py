_E='read-write'
_D='h3cMACsecCFGPortIndex'
_C='H3C-MACSEC-MIB'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cMACsec=ModuleIdentity((1,3,6,1,4,1,2011,10,2,163))
if mibBuilder.loadTexts:h3cMACsec.setRevisions(('2015-09-01 16:15',))
_H3cMACsecCFGObjects_ObjectIdentity=ObjectIdentity
h3cMACsecCFGObjects=_H3cMACsecCFGObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,163,1))
_H3cMACsecCFGPortTable_Object=MibTable
h3cMACsecCFGPortTable=_H3cMACsecCFGPortTable_Object((1,3,6,1,4,1,2011,10,2,163,1,1))
if mibBuilder.loadTexts:h3cMACsecCFGPortTable.setStatus(_A)
_H3cMACsecCFGPortEntry_Object=MibTableRow
h3cMACsecCFGPortEntry=_H3cMACsecCFGPortEntry_Object((1,3,6,1,4,1,2011,10,2,163,1,1,1))
h3cMACsecCFGPortEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:h3cMACsecCFGPortEntry.setStatus(_A)
_H3cMACsecCFGPortIndex_Type=InterfaceIndex
_H3cMACsecCFGPortIndex_Object=MibTableColumn
h3cMACsecCFGPortIndex=_H3cMACsecCFGPortIndex_Object((1,3,6,1,4,1,2011,10,2,163,1,1,1,1),_H3cMACsecCFGPortIndex_Type())
h3cMACsecCFGPortIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cMACsecCFGPortIndex.setStatus(_A)
class _H3cMACsecCFGPortPSKCKNName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_H3cMACsecCFGPortPSKCKNName_Type.__name__=_B
_H3cMACsecCFGPortPSKCKNName_Object=MibTableColumn
h3cMACsecCFGPortPSKCKNName=_H3cMACsecCFGPortPSKCKNName_Object((1,3,6,1,4,1,2011,10,2,163,1,1,1,2),_H3cMACsecCFGPortPSKCKNName_Type())
h3cMACsecCFGPortPSKCKNName.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMACsecCFGPortPSKCKNName.setStatus(_A)
class _H3cMACsecCFGPortPSKCAKValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_H3cMACsecCFGPortPSKCAKValue_Type.__name__=_B
_H3cMACsecCFGPortPSKCAKValue_Object=MibTableColumn
h3cMACsecCFGPortPSKCAKValue=_H3cMACsecCFGPortPSKCAKValue_Object((1,3,6,1,4,1,2011,10,2,163,1,1,1,3),_H3cMACsecCFGPortPSKCAKValue_Type())
h3cMACsecCFGPortPSKCAKValue.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMACsecCFGPortPSKCAKValue.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'h3cMACsec':h3cMACsec,'h3cMACsecCFGObjects':h3cMACsecCFGObjects,'h3cMACsecCFGPortTable':h3cMACsecCFGPortTable,'h3cMACsecCFGPortEntry':h3cMACsecCFGPortEntry,_D:h3cMACsecCFGPortIndex,'h3cMACsecCFGPortPSKCKNName':h3cMACsecCFGPortPSKCKNName,'h3cMACsecCFGPortPSKCAKValue':h3cMACsecCFGPortPSKCAKValue})