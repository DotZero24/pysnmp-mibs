_G='devAtmAutoConfigXconChannel'
_F='devAtmMaxVpi'
_E='devAtmMaxIfIndex'
_D='read-only'
_C='PDN-SCMEXT-MIB'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pdnAtm,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdnAtm')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
_DevAtmScm_ObjectIdentity=ObjectIdentity
devAtmScm=_DevAtmScm_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,4))
_DevAtmMaxVciVpiConfig_ObjectIdentity=ObjectIdentity
devAtmMaxVciVpiConfig=_DevAtmMaxVciVpiConfig_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,4,1))
_DevAtmMaxVciVpiConfigTable_Object=MibTable
devAtmMaxVciVpiConfigTable=_DevAtmMaxVciVpiConfigTable_Object((1,3,6,1,4,1,1795,2,24,2,6,11,4,1,1))
if mibBuilder.loadTexts:devAtmMaxVciVpiConfigTable.setStatus(_A)
_DevAtmMaxVciVpiConfigEntry_Object=MibTableRow
devAtmMaxVciVpiConfigEntry=_DevAtmMaxVciVpiConfigEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,11,4,1,1,1))
devAtmMaxVciVpiConfigEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:devAtmMaxVciVpiConfigEntry.setStatus(_A)
_DevAtmMaxIfIndex_Type=Integer32
_DevAtmMaxIfIndex_Object=MibTableColumn
devAtmMaxIfIndex=_DevAtmMaxIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,11,4,1,1,1,1),_DevAtmMaxIfIndex_Type())
devAtmMaxIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:devAtmMaxIfIndex.setStatus(_A)
_DevAtmMaxVpi_Type=Integer32
_DevAtmMaxVpi_Object=MibTableColumn
devAtmMaxVpi=_DevAtmMaxVpi_Object((1,3,6,1,4,1,1795,2,24,2,6,11,4,1,1,1,2),_DevAtmMaxVpi_Type())
devAtmMaxVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:devAtmMaxVpi.setStatus(_A)
_DevAtmMaxVci_Type=Integer32
_DevAtmMaxVci_Object=MibTableColumn
devAtmMaxVci=_DevAtmMaxVci_Object((1,3,6,1,4,1,1795,2,24,2,6,11,4,1,1,1,3),_DevAtmMaxVci_Type())
devAtmMaxVci.setMaxAccess(_B)
if mibBuilder.loadTexts:devAtmMaxVci.setStatus(_A)
_DevAtmMaxVciVpiRowStatus_Type=RowStatus
_DevAtmMaxVciVpiRowStatus_Object=MibTableColumn
devAtmMaxVciVpiRowStatus=_DevAtmMaxVciVpiRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,11,4,1,1,1,4),_DevAtmMaxVciVpiRowStatus_Type())
devAtmMaxVciVpiRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:devAtmMaxVciVpiRowStatus.setStatus(_A)
_DevAtmAutoConfigXcon_ObjectIdentity=ObjectIdentity
devAtmAutoConfigXcon=_DevAtmAutoConfigXcon_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,4,2))
_DevAtmAutoConfigXconTable_Object=MibTable
devAtmAutoConfigXconTable=_DevAtmAutoConfigXconTable_Object((1,3,6,1,4,1,1795,2,24,2,6,11,4,2,1))
if mibBuilder.loadTexts:devAtmAutoConfigXconTable.setStatus(_A)
_DevAtmAutoConfigXconEntry_Object=MibTableRow
devAtmAutoConfigXconEntry=_DevAtmAutoConfigXconEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,11,4,2,1,1))
devAtmAutoConfigXconEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:devAtmAutoConfigXconEntry.setStatus(_A)
_DevAtmAutoConfigXconChannel_Type=Integer32
_DevAtmAutoConfigXconChannel_Object=MibTableColumn
devAtmAutoConfigXconChannel=_DevAtmAutoConfigXconChannel_Object((1,3,6,1,4,1,1795,2,24,2,6,11,4,2,1,1,1),_DevAtmAutoConfigXconChannel_Type())
devAtmAutoConfigXconChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:devAtmAutoConfigXconChannel.setStatus(_A)
_DevAtmAutoConfigXconIfIndex_Type=Integer32
_DevAtmAutoConfigXconIfIndex_Object=MibTableColumn
devAtmAutoConfigXconIfIndex=_DevAtmAutoConfigXconIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,11,4,2,1,1,2),_DevAtmAutoConfigXconIfIndex_Type())
devAtmAutoConfigXconIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:devAtmAutoConfigXconIfIndex.setStatus(_A)
_DevAtmAutoConfigXconVpi_Type=Integer32
_DevAtmAutoConfigXconVpi_Object=MibTableColumn
devAtmAutoConfigXconVpi=_DevAtmAutoConfigXconVpi_Object((1,3,6,1,4,1,1795,2,24,2,6,11,4,2,1,1,3),_DevAtmAutoConfigXconVpi_Type())
devAtmAutoConfigXconVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:devAtmAutoConfigXconVpi.setStatus(_A)
_DevAtmAutoConfigXconVci_Type=Integer32
_DevAtmAutoConfigXconVci_Object=MibTableColumn
devAtmAutoConfigXconVci=_DevAtmAutoConfigXconVci_Object((1,3,6,1,4,1,1795,2,24,2,6,11,4,2,1,1,4),_DevAtmAutoConfigXconVci_Type())
devAtmAutoConfigXconVci.setMaxAccess(_B)
if mibBuilder.loadTexts:devAtmAutoConfigXconVci.setStatus(_A)
_DevAtmAutoConfigXconTraffic_Type=Integer32
_DevAtmAutoConfigXconTraffic_Object=MibTableColumn
devAtmAutoConfigXconTraffic=_DevAtmAutoConfigXconTraffic_Object((1,3,6,1,4,1,1795,2,24,2,6,11,4,2,1,1,5),_DevAtmAutoConfigXconTraffic_Type())
devAtmAutoConfigXconTraffic.setMaxAccess(_B)
if mibBuilder.loadTexts:devAtmAutoConfigXconTraffic.setStatus(_A)
_DevAtmAutoConfigXconRowStatus_Type=RowStatus
_DevAtmAutoConfigXconRowStatus_Object=MibTableColumn
devAtmAutoConfigXconRowStatus=_DevAtmAutoConfigXconRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,11,4,2,1,1,6),_DevAtmAutoConfigXconRowStatus_Type())
devAtmAutoConfigXconRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:devAtmAutoConfigXconRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'devAtmScm':devAtmScm,'devAtmMaxVciVpiConfig':devAtmMaxVciVpiConfig,'devAtmMaxVciVpiConfigTable':devAtmMaxVciVpiConfigTable,'devAtmMaxVciVpiConfigEntry':devAtmMaxVciVpiConfigEntry,_E:devAtmMaxIfIndex,_F:devAtmMaxVpi,'devAtmMaxVci':devAtmMaxVci,'devAtmMaxVciVpiRowStatus':devAtmMaxVciVpiRowStatus,'devAtmAutoConfigXcon':devAtmAutoConfigXcon,'devAtmAutoConfigXconTable':devAtmAutoConfigXconTable,'devAtmAutoConfigXconEntry':devAtmAutoConfigXconEntry,_G:devAtmAutoConfigXconChannel,'devAtmAutoConfigXconIfIndex':devAtmAutoConfigXconIfIndex,'devAtmAutoConfigXconVpi':devAtmAutoConfigXconVpi,'devAtmAutoConfigXconVci':devAtmAutoConfigXconVci,'devAtmAutoConfigXconTraffic':devAtmAutoConfigXconTraffic,'devAtmAutoConfigXconRowStatus':devAtmAutoConfigXconRowStatus})